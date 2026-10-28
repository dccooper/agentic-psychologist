"""Match each numbered script line to its take in the transcribed recordings.

usage: python align.py SCRIPT.md OUT.json REC1.json:1-10 REC2.json:11-14 PICKUP.json:14a ...

SCRIPT.md holds lines written as **N.** text (the voiceover script); a line added later
can take a letter, like **14a.**, so nothing gets renumbered. Each REC is a transcript
from transcribe.py plus the script lines read in that recording: a range (1-10) or one id.
For every line it finds the best-matching stretch of words. When a line was read more
than once (a retake), it keeps the last good take before the next line starts.
The output lists, per line: recording, start and end time, and the words as spoken.
"""
import json, os, re, sys
from difflib import SequenceMatcher

GOOD = 0.5          # similarity needed to count as a reading of the line
MAX_GAP = 1.3       # a pause longer than this (seconds) ends the take
OVERRIDES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "overrides.json")

def norm(w):
    w = w.lower().replace("anti-gravity", "antigravity").replace("’", "'")
    return re.sub(r"[^a-z0-9']", "", w)

def script_lines(path):
    lines = {}
    for m in re.finditer(r"^\*\*(\d+[a-z]?)\.\*\*\s+(?:\[STRAIGHT\]\s*)?(.+)$", open(path, encoding="utf-8").read(), re.M):
        lines[m.group(1)] = m.group(2).strip()
    return lines

def words_of(rec):
    out = []
    for seg in json.load(open(rec, encoding="utf-8")):
        ws = seg["words"]
        # Known Whisper failure modes: a phantom repeat of a sentence squeezed into zero
        # time (mostly zero-length words: drop the segment), stray zero-length words inside
        # real speech (drop those words, but keep a segment's first word), and a lone
        # "word" that is really a click or breath.
        zero = [e - s <= 0.0 for s, e, _ in ws]
        if len(ws) >= 3 and sum(zero) > len(ws) / 2: continue
        if len(ws) == 1 and ws[0][1] - ws[0][0] < 0.4: continue
        for k, (s, e, w) in enumerate(ws):
            if zero[k] and k > 0: continue
            if w.startswith("-") and out:      # Whisper splits "Anti-Gravity" into "Anti" + "-Gravity"
                out[-1].update(e=e, w=out[-1]["w"] + w.strip(), n=norm(out[-1]["w"] + w)); continue
            out.append({"s": s, "e": e, "w": w.strip(), "n": norm(w)})
    return [w for w in out if w["n"]]

def score(words, i, target):
    got = [w["n"] for w in words[i:i + len(target)]]
    return SequenceMatcher(None, got, target, autojunk=False).ratio()

def matches(words, start, target, anchor=2):
    """Start positions of distinct takes of `target`, earliest first.

    Neighbouring start positions all score well inside one take, so candidates close
    together are grouped and each group keeps its best start (the earliest on a tie).
    """
    cand = [(i, score(words, i, target)) for i in range(start, len(words))
            if anchor is None or words[i]["n"] in target[:anchor]]
    cand = [(i, s) for i, s in cand if s >= GOOD]
    takes, group = [], []
    for i, s in cand:
        if group and i - group[-1][0] > max(3, len(target) // 2):
            takes.append(group); group = []
        group.append((i, s))
    if group: takes.append(group)
    # Within a take, prefer the earliest start that scores nearly as well as the best:
    # a misheard opening word ("dot com" for "slash download") shouldn't cost the opening.
    # The earlier start must run on without a long pause; otherwise it's the previous line's tail.
    def joined(i, j):
        return all(words[k + 1]["s"] - words[k]["e"] < MAX_GAP for k in range(i, j))
    out = []
    for g in takes:
        best = max(g, key=lambda c: c[1])
        out.append(next(i for i, s in g if s >= best[1] - 0.12 and joined(i, best[0])))
    return out

def take_end(words, i, stop):
    j = i
    while j + 1 < stop and words[j + 1]["s"] - words[j]["e"] < MAX_GAP:
        j += 1
    return j

def align(script, rec, ids):
    words, out, cursor = words_of(rec), [], 0
    for k, n in enumerate(ids):
        target = [norm(w) for w in script[n].split() if norm(w)]
        found = matches(words, cursor, target) or matches(words, cursor, target, anchor=None)
        if not found:
            print(f"line {n}: no take found in {rec}", file=sys.stderr); continue
        # A weaker match in the middle of a continuous take is the line repeating a word
        # ("That's orientation… That's roughly how long"), not a retake.
        kept = [found[0]]
        for i in found[1:]:
            p = kept[-1]
            if i <= take_end(words, p, len(words)) and score(words, i, target) < score(words, p, target) - 0.15:
                continue
            kept.append(i)
        found = kept
        first = found[0]
        nxt = len(words)
        if k + 1 < len(ids):
            t2 = [norm(w) for w in script[ids[k + 1]].split() if norm(w)]
            later = [i for i in matches(words, first + 1, t2) if i > first]
            if later: nxt = later[0]
        best = [i for i in found if i < nxt][-1]          # last take before the next line
        while best > cursor and words[best]["s"] - words[best - 1]["e"] < 0.35:
            best -= 1                                      # same breath: "You can press Tab..."
        end = take_end(words, best, nxt)
        takes = len([i for i in found if i < nxt])
        span = words[best:end + 1]
        out.append({"line": n, "rec": rec, "start": span[0]["s"], "end": span[-1]["e"], "takes": takes,
                    "score": round(score(words, best, target), 2), "text": " ".join(w["w"] for w in span),
                    "words": [[w["s"], w["e"], w["w"]] for w in span]})
        cursor = end + 1
    return out

if __name__ == "__main__":
    script = script_lines(sys.argv[1])
    result = []
    overrides = {}
    if os.path.exists(OVERRIDES):
        overrides = {k: v for k, v in json.load(open(OVERRIDES, encoding="utf-8")).items() if not k.startswith("_")}
    for arg in sys.argv[3:]:
        rec, rng = arg.rsplit(":", 1)
        if "-" in rng:
            a, b = map(int, rng.split("-")); ids = [str(i) for i in range(a, b + 1)]
        else:
            ids = [rng]
        result += align(script, rec, ids)
    for r in result:                                   # hand corrections where the transcript's timing is wrong
        o = overrides.get(r["line"], {})
        if "rec" in o and os.path.basename(r["rec"]).replace(".json", "") != o["rec"]:
            o = {}                                     # the fix belongs to another recording of this line
        if "start" in o:                               # words timed before the new start move up to it
            r["start"] = o["start"]
            for w in r["words"]:
                if w[0] < o["start"]: w[0] = o["start"]; w[1] = max(w[1], o["start"])
            r["words"][0][0] = o["start"]
        if "end" in o: r["end"] = o["end"]
        if o: r["override"] = o.get("why", True)
    json.dump(result, open(sys.argv[2], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for r in result:
        flag = "" if r["score"] >= 0.75 else "  <- check (ad-lib or mismatch)"
        print(f"{r['line']:>2}  {r['start']:7.2f}-{r['end']:7.2f}  takes={r['takes']}  score={r['score']}{flag}\n     {r['text']}")
