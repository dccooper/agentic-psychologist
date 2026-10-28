# Orientation video

The source for the setup page's orientation video. The full story (script, design decisions, sound, how to restyle or translate) is on the course site: **[How the video was made](https://dccooper.github.io/agentic-psychologist/video/)** ([`docs/video.md`](../docs/video.md)).

| File | What it is |
|---|---|
| `script.en.md` | The voiceover script, numbered lines |
| `orientation.html` | The video as a web page: design tokens, then one block per scene |
| `strings.en.js` | Every word on screen, caption spelling fixes, and the words each animation is pinned to |
| `render.mjs` | Draws every frame in Chrome and encodes with ffmpeg |
| `pipeline/` | Audio: `transcribe.py` → `align.py` → `build_audio.py`, plus `scenes.json` and `overrides.json` |
| `transcripts/en/` | Word-timed transcripts of the English recordings |
| `build/en/cues.js`, `captions.srt` | Generated timing and captions (committed, so you can restyle without the audio) |

Not in the repo: the recordings (`media/`), the narrator's photo (`assets/author.jpg`; a placeholder shows instead), the music file, and rendered videos.

```bash
npm install
node render.mjs --stills 12,95,240     # check frames (works from the committed cues)
node render.mjs --preview              # 960×540 draft (needs build/en/mix.wav)
node render.mjs                        # final 1920×1080
```
