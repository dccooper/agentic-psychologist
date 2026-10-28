"""Transcribe voiceover recordings with word-level timestamps (faster-whisper).

usage: python transcribe.py OUT_DIR REC1.wav [REC2.wav ...] [--model large-v3] [--lang en]

Writes OUT_DIR/<recording name>.json: a list of segments, each with start, end, text and
words as [start, end, word]. align.py reads these. Uses the GPU when one is available.
The large-v3 model is about 3 GB; a copy already in the Hugging Face cache is used as is.
"""
import glob, json, os, sys
from faster_whisper import WhisperModel

args = sys.argv[1:]
def opt(name, default):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return default
model_name, lang = opt("--model", "large-v3"), opt("--lang", "en")
out_dir, recordings = args[0], args[1:]

# Prefer a model already on disk (no network needed); otherwise let faster-whisper fetch it
cached = glob.glob(os.path.expanduser(f"~/.cache/huggingface/hub/models--Systran--faster-whisper-{model_name}/snapshots/*/"))
model_ref = cached[0] if cached else model_name
try:
    m = WhisperModel(model_ref, device="cuda", compute_type="float16")
    list(m.transcribe(recordings[0], beam_size=1, clip_timestamps=[0, 5])[0])   # probe the GPU
    print("using GPU", file=sys.stderr)
except Exception as e:
    print("GPU unavailable, using CPU (slower):", e, file=sys.stderr)
    m = WhisperModel(model_ref, device="cpu", compute_type="int8")

os.makedirs(out_dir, exist_ok=True)
for src in recordings:
    segs, _ = m.transcribe(src, word_timestamps=True, beam_size=5, language=lang)
    out = [{"start": s.start, "end": s.end, "text": s.text.strip(),
            "words": [[w.start, w.end, w.word] for w in s.words]} for s in segs]
    name = os.path.basename(src).rsplit(".", 1)[0]
    json.dump(out, open(os.path.join(out_dir, name + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"== {name}", flush=True)
    for s in out:
        print(f"{s['start']:7.2f}-{s['end']:7.2f}  {s['text']}", flush=True)
