"""Cut the chosen take of every line out of the recordings, clean up the voice,
lay everything on one timeline, and mix in the music bed.

usage: python build_audio.py ALIGNED.json SCENES.json REC_DIR OUT_DIR [--music FILE.mp3]

ALIGNED.json comes from align.py. SCENES.json lists the scenes in order, each with the
script lines it covers. REC_DIR holds the original .wav recordings (same base names as
the transcripts). Writes to OUT_DIR:
  voice.wav  the edited, cleaned voiceover (mono, 48 kHz, -16 LUFS)
  mix.wav    voice plus music, what the video uses
  cues.js    line timings and spoken words on the final timeline, read by the composition
"""
import json, os, subprocess, sys, wave
import numpy as np

RATE = 48000
LEAD_IN = 1.6        # title card plays alone before the first word
GAP_LINE = 0.45      # silence between lines in the same scene
GAP_SCENE = 1.0      # between scenes, so each change of picture gets a beat
TAIL = 3.0           # end card holds after the last word
PRE, POST = 0.12, 0.15   # air kept around each take, after snapping to the waveform

# Voice clean-up, in order: rumble filter, gentle noise reduction, a little warmth,
# soften the harsh 3-4 kHz band, tame "s" sounds, even out the level, then normalise.
VOICE_CHAIN = ",".join([
    "highpass=f=80",
    "afftdn=nr=8:nf=-45:tn=1",
    "equalizer=f=180:t=q:w=1.0:g=1.5",
    "equalizer=f=3400:t=q:w=1.2:g=-3",
    "equalizer=f=7500:t=q:w=1.5:g=-1.5",
    "deesser=i=0.5:m=0.5:f=0.5",
    "acompressor=threshold=0.1:ratio=3:attack=15:release=200:makeup=1.5",
])
VOICE_LUFS = -16     # common target for online video
MUSIC_BELOW = 27     # music sits this many dB (LU) under the voice
MUSIC_FADE = 2.0
MUSIC_OFF = {"straight"}   # scenes with no music: the out-of-character aside

def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(RATE), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)

def fade(x, n=int(0.012 * RATE)):
    x = x.copy(); r = np.linspace(0, 1, min(n, len(x) // 2))
    x[:len(r)] *= r; x[len(x) - len(r):] *= r[::-1]
    return x

# ── Snapping: the transcript's word times are close but often end a word early.
# Each cut moves to where the waveform actually starts or stops being speech.
HOP = int(0.01 * RATE)
def envelope(x):
    n = len(x) // HOP
    rms = np.sqrt(np.mean(x[:n * HOP].reshape(n, HOP) ** 2, axis=1) + 1e-12)
    return 20 * np.log10(rms)

def speech_threshold(env):
    floor = np.percentile(env, 10)            # room noise between lines
    return max(floor + 12, -62)            # low enough to keep soft first and last consonants

def snap_end(env, thr, t, limit, quiet=0.25):
    i, stop, q = int(t * 100), int(min(limit, t + 2.5) * 100), int(quiet * 100)
    while i < stop and i + q <= len(env):
        if np.all(env[i:i + q] < thr): return i / 100
        i += 1
    return min(limit, t + 2.5)

def snap_start(env, thr, t, limit, quiet=0.15):
    i, q = int(t * 100), int(quiet * 100)
    if env[min(i, len(env) - 1)] < thr:        # transcript starts in silence: move to the onset
        j = i
        while j < min(len(env), i + 60) and env[j] < thr: j += 1
        return j / 100 if j < i + 60 else t
    lo = int(max(limit, t - 1.0) * 100)       # inside speech: back up to the silence before it
    while i > lo and not np.all(env[max(0, i - q):i] < thr): i -= 1
    return i / 100

def loudnorm(src, dst, target, pre_filters=""):
    """Two-pass EBU R128 loudness normalisation (measure, then apply linearly)."""
    chain = (pre_filters + "," if pre_filters else "")
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-af", chain + f"loudnorm=I={target}:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    second = (f"loudnorm=I={target}:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
              f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", chain + second, "-ar", str(RATE), "-ac", "1", dst], check=True)

def write_wav(path, x):
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())

args = sys.argv[1:]
music = args[args.index("--music") + 1] if "--music" in args else None
aligned, scenes_path, rec_dir, out_dir = [a for a in args if a not in ("--music", music)][:4]
takes = {str(t["line"]): t for t in json.load(open(aligned, encoding="utf-8"))}
scenes = json.load(open(scenes_path, encoding="utf-8"))
os.makedirs(out_dir, exist_ok=True)

# Clean each recording once, whole, so the noise reducer and compressor see real context
audio, envs = {}, {}
def source(rec):
    src = os.path.join(rec_dir, os.path.basename(rec).replace(".json", ".wav"))
    if src not in audio:
        clean = os.path.join(out_dir, "clean-" + os.path.basename(src))
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-ac", "1", "-ar", str(RATE), "-af", VOICE_CHAIN, clean], check=True)
        audio[src] = load(clean); envs[src] = envelope(load(src))
        os.remove(clean)
    return src

# Neighbouring takes in the same recording bound how far a cut may move
by_rec = {}
for t in takes.values(): by_rec.setdefault(t["rec"], []).append(t)
for lst in by_rec.values(): lst.sort(key=lambda t: t["start"])
def bounds(tk):
    lst = by_rec[tk["rec"]]; i = lst.index(tk)
    return (lst[i - 1]["end"] + 0.05 if i else 0.0), (lst[i + 1]["start"] - 0.05 if i + 1 < len(lst) else 1e9)

report = []
pieces, t, cues = [np.zeros(int(LEAD_IN * RATE), np.float32)], LEAD_IN, {"lines": {}, "scenes": []}
for si, sc in enumerate(scenes):
    if si: pieces.append(np.zeros(int(GAP_SCENE * RATE), np.float32)); t += GAP_SCENE
    s_start = t if si else 0.0
    for li, n in enumerate(sc["lines"]):
        n = str(n)
        if n not in takes: sys.exit(f"line {n} has no take; fix the alignment first")
        tk = takes[n]
        if li: pieces.append(np.zeros(int(GAP_LINE * RATE), np.float32)); t += GAP_LINE
        src = source(tk["rec"]); env = envs[src]; thr = speech_threshold(env)
        lo, hi = bounds(tk)
        start = tk["start"] if "override" in tk else snap_start(env, thr, tk["start"], lo)
        end = snap_end(env, thr, tk["end"], min(hi, len(env) / 100))
        report.append((n, start - tk["start"], end - tk["end"]))
        a, b = max(0, start - PRE), end + POST
        clip = fade(audio[src][int(a * RATE):int(b * RATE)])
        shift = t - a
        cues["lines"][n] = {"start": round(start + shift, 3), "end": round(end + shift, 3),
                            "words": [[round(s + shift, 3), round(e + shift, 3), w] for s, e, w in tk["words"]]}
        pieces.append(clip); t += len(clip) / RATE
    cues["scenes"].append({"id": sc["id"], "start": round(s_start, 3)})
pieces.append(np.zeros(int(TAIL * RATE), np.float32)); t += TAIL
for i, sc in enumerate(cues["scenes"]):
    sc["end"] = cues["scenes"][i + 1]["start"] if i + 1 < len(cues["scenes"]) else round(t, 3)
cues["duration"] = round(t, 3)

rough = os.path.join(out_dir, "voice-rough.wav")
write_wav(rough, np.concatenate(pieces))
voice_path = os.path.join(out_dir, "voice.wav")
loudnorm(rough, voice_path, VOICE_LUFS)
os.remove(rough)

# ── Music bed: plays under everything except the out-of-character aside, where it
# fades out, then picks up where it paused when the character returns.
mix_path = os.path.join(out_dir, "mix.wav")
if music:
    mq = os.path.join(out_dir, "music-level.wav")
    loudnorm(music, mq, VOICE_LUFS - MUSIC_BELOW)
    m = load(mq); os.remove(mq)
    bed, pos = np.zeros(int(t * RATE), np.float32), 0
    spans = []                                  # (start, end) of the stretches with music
    for sc in cues["scenes"]:
        on = sc["id"] not in MUSIC_OFF
        if on and spans and abs(spans[-1][1] - sc["start"]) < 1e-6: spans[-1][1] = sc["end"]
        elif on: spans.append([sc["start"], sc["end"]])
    for a, b in spans:
        n = min(int((b - a) * RATE), len(bed) - int(a * RATE)); seg = m[pos:pos + n]
        if len(seg) < n: seg = np.concatenate([seg, m[:n - len(seg)]])   # loop if the track runs out
        f = int(MUSIC_FADE * RATE); env_ = np.ones(n, np.float32)
        if a > 0: env_[:f] = np.linspace(0, 1, f)
        env_[-f:] = np.linspace(1, 0, f)
        bed[int(a * RATE):int(a * RATE) + n] = seg * env_; pos += n
    v = load(voice_path)
    write_wav(mix_path, v[:len(bed)] + bed[:len(v)])
    cues["music"] = [[round(a, 3), round(b, 3)] for a, b in spans]
else:
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", voice_path, mix_path], check=True)

open(os.path.join(out_dir, "cues.js"), "w", encoding="utf-8").write(
    "// Generated by build_audio.py. Do not edit by hand; re-run the pipeline.\nwindow.CUES = " +
    json.dumps(cues, ensure_ascii=False) + ";\n")
print(f"voice.wav and mix.wav: {t:.1f}s, {len(cues['lines'])} lines, {len(cues['scenes'])} scenes")
for n, ds, de in report:                                # how far snapping moved each cut
    print(f"  line {n:>3}: start {ds:+.2f}s, end {de:+.2f}s")
