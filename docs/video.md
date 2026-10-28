---
title: How the video was made
nav_order: 8
description: How the orientation video was scripted, recorded, edited, designed and rendered, and how to change, restyle or translate it.
---

# How the orientation video was made
{: .no_toc }

The setup page opens with a six-minute orientation video. Everything that produced it is in this repository, in the [`video/`](https://github.com/dccooper/agentic-psychologist/tree/main/video) folder, so you can fix a line, restyle it, or make it in another language. This page explains how it was made and the decisions behind it.

<details open markdown="block">
  <summary>On this page</summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## The short version

The video is a web page. [`video/orientation.html`](https://github.com/dccooper/agentic-psychologist/blob/main/video/orientation.html) draws any moment of the video when asked "what does second *t* look like?". A script opens the page in Chrome, asks for every frame in turn (30 per second), and hands the frames to ffmpeg, which joins them with the soundtrack into an MP4.

Nothing is hand-animated in a video editor. The voice recording drives the timing: speech-to-text finds when each word was said, and the animations are pinned to those words. Re-record a line and the picture follows.

```
recordings (.wav) ─► transcribe.py ─► align.py ─► build_audio.py ─► cues.js + mix.wav
                     (word timings)  (which take   (cut, clean up,       │
                                      is each line)  add music)          ▼
                           strings.en.js ─► orientation.html ─► render.mjs ─► orientation.mp4
                           (all on-screen text)  (the scenes)    (Chrome + ffmpeg)  + captions.srt
```

## The script

The voiceover script is [`video/script.en.md`](https://github.com/dccooper/agentic-psychologist/blob/main/video/script.en.md): 31 numbered lines in ten scenes, with notes on what's on screen.

- **The narrator is a character.** M. Pending, Acting Deputy Assistant Registrar (provisionally), is the memo-writer from the home page.
- **The course's humor rule applies.** Jokes land on the institution (the coffee machine, Procrastination Hall, the font size on Google's download page), never on the learner.
- **One stretch is played straight.** Lines 11–14 (security, the one rule about real data, the data-sharing checkbox, cost) step out of character. The author appears in person, and the music stops.
- **Line numbers are the glue.** Scenes, visual cues and timing fixes all refer to lines by number. A line added later gets a letter (**14a.**, the "picking up where we left off" pickup), so nothing has to be renumbered.

The narrator ad-libbed in places. The captions follow what was said, not the script.

## Look and feel: "polished wireframe"

The app screens in the video are drawings, not screenshots. Skeleton bars stand in for text you don't need to read.

- **It doesn't go stale.** Antigravity updates often. A drawing of "the agent panel is on the right" stays true longer than a screenshot of this month's panel.
- **It points at what matters.** The first look teaches three parts of the window. Everything else is drawn as grey bars, then hatched out as "Ignore for now."
- **It matches the course site.** The colors are the site's "Harbor" palette, and the type is Atkinson Hyperlegible, a typeface designed for readability.

Design tokens (colors, fonts, corner radius, shadows) are CSS variables at the top of `orientation.html`. Change them there and every scene follows.

| Element | Treatment |
|---|---|
| Captions | Always on, burned in: a dark plate at the bottom, 35 px, at most two lines. The bottom of the frame is kept clear for them. |
| Supporting text (chips, notes, step labels) | 27–31 px, so it reads at phone size |
| Highlights | A spotlight that dims everything else, or a ring around one control |
| Motion | Things rise in, spring in ("pop"), or slide; outgoing scenes lift slightly as they fade. Mouse clicks show a ripple, and key presses show a 3D keycap. |
| Jokes | A rubber stamp (PROVISIONALLY), sticky notes (coffee machine out of order), a progress bar stuck at 99% |

### The scenes

| Scene | Lines | What you see |
|---|---|---|
| Title | 1–2 | Crest, department, "New Student Orientation (Video)"; M. Pending's name card and stamp |
| Download | 3–5 | A browser on the download page: the wrong app crossed out, a scroll down to the small "Antigravity IDE (Standalone)" heading, the right button ringed for each kind of computer |
| Install | 6–8 | Windows installer and Mac drag-to-Applications side by side; Procrastination Hall installing |
| Sign in | 9–10 | "Continue with Google", then the setup screens, with Review-driven development chosen |
| Out of character | 11–14 | The author's photo pops in, then shrinks to a corner; the security notice, the one rule, the data checkbox being unticked, the free plan |
| Pickup | 14a | M. Pending returns; a tracker shows steps 1–3 done and step 4 next |
| Get the course | 15–17 | Extract the ZIP (Windows) or double-click (Mac), Open Folder, trust the authors |
| First look | 18–25 | The Antigravity window; agent panel, Explorer and editor in turn; typing `/sta`, Tab, Enter; waiting |
| Accept or reject | 26–27 | A proposed change with Accept and Reject; a trainee's note being signed |
| End | 28–30 | "From here, the tutor takes over", `/im-stuck`, `/my-progress`, the site address, the music credit |

## Sound

### Voice

The narration was recorded as four WAV files, read line by line with a pause between lines, plus one pickup recorded later. The pipeline then:

1. **Transcribes** each file with word timestamps (faster-whisper, `large-v3` model, run locally).
2. **Matches every script line to its take.** When a line was read twice, the last good take wins. When a flub and its retake were heard as one take, a hand correction in [`pipeline/overrides.json`](https://github.com/dccooper/agentic-psychologist/blob/main/video/pipeline/overrides.json) moves the start, with a note saying why.
3. **Cuts each take where the sound actually starts and stops.** Speech-to-text tends to end a word early, which clipped the last word of lines. Cuts now snap to the waveform.
4. **Closes up the pauses.** The 2-second recording pauses become 0.45 s between lines and 1 s between scenes.
5. **Cleans up the voice** with a standard voiceover chain: rumble filter (80 Hz), light noise reduction, a touch of warmth (180 Hz), a softened harsh band (−3 dB at 3.4 kHz), de-esser, gentle compression (3:1).
6. **Sets the loudness** to −16 LUFS, a common target for online video.

### Music

"Wholesome" by Kevin MacLeod ([incompetech.com](https://incompetech.com)), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It sits 27 dB under the voice, so it's there but never competes. It fades out for the out-of-character stretch and resumes where it paused when M. Pending returns.

CC BY 4.0 works with this course's CC BY-SA 4.0 content license, as long as the music is credited. The credit is on the end card and in the video's YouTube description. Edits made: level lowered, faded, paused under the aside.

## What's in the repository, and what isn't

| In the repo | Kept out, and why |
|---|---|
| The composition, strings, script, renderer and audio pipeline | Voice recordings: the author's own; a new version needs new recordings anyway |
| Transcripts of the recordings (`transcripts/en/`) | The author's photo (`assets/author.jpg`): a person's likeness isn't covered by the course's open license; a placeholder shows instead |
| The generated cue sheet and captions (`build/en/cues.js`, `captions.srt`), so you can restyle and check frames without the audio | The music file: download it from incompetech (free, CC BY) |
| | Rendered video: it lives on YouTube |

## Make it yourself

You need [Node.js](https://nodejs.org) 18+, [Python](https://www.python.org) 3.10+ with `numpy` and `faster-whisper`, [ffmpeg](https://ffmpeg.org), and Google Chrome. A GPU makes transcription faster but isn't required. Run commands from the `video/` folder.

```bash
npm install                                  # once: installs playwright-core

# Look at any moment without rendering: open orientation.html?t=95 in Chrome,
# or save PNG frames:
node render.mjs --stills 12,95,240

# Rebuild from recordings (put your WAVs in media/en/):
python pipeline/transcribe.py transcripts/en media/en/*.wav
python pipeline/align.py script.en.md pipeline/aligned.json \
  transcripts/en/overview_video_lines_1-10.json:1-10 \
  transcripts/en/straight_interjection_lines11-14.json:11-14 \
  transcripts/en/Picking_up.json:14a \
  transcripts/en/overview_video_lines_15-30.json:15-30
python pipeline/build_audio.py pipeline/aligned.json pipeline/scenes.json media/en build/en --music media/Wholesome.mp3

node render.mjs --preview                    # quick: 960×540, 24 fps, ~3 minutes
node render.mjs                              # final: 1920×1080, 30 fps → build/en/orientation.mp4
```

`align.py` prints each line's take with a match score and flags low scores. Ad-libs score lower, which is fine; read the flagged lines to be sure the right take was picked. If Chrome isn't in its usual Windows location, set the `CHROME` environment variable to its path.

## Common changes

**Fix a word on screen.** Edit [`strings.en.js`](https://github.com/dccooper/agentic-psychologist/blob/main/video/strings.en.js) (the `ui` section). All on-screen text lives there; the scenes contain none.

**Fix a caption.** Captions come from what was said. To correct the speech-to-text's spelling, add a rule to `captionFixes` in `strings.en.js`; for example, it heard "golf machine" for "coffee machine".

**Re-record a line.** Record it alone, transcribe it, and pass it to `align.py` as `pickup.json:17`, after the recording it replaces. Delete any entry for that line in `overrides.json`.

**Move an animation.** Visual beats are pinned to spoken words in `anchors` (in `strings.en.js`). For example, `intel: [5, "intel"]` means "when *Intel* is said in line 5". Change the word, or add seconds as a third value.

**Restyle.** Change the tokens at the top of `orientation.html`. Each scene's layout is in its own `SCENES.<name>` block, which has a `build()` that returns the scene's HTML and a `draw(t)` that positions everything at time `t`.

**Swap the music.** Pass a different file to `--music`, and update `musicCredit` in `strings.en.js` to match its license. The level and fades are set in `build_audio.py`.

## Translate it

1. **Translate the script.** Copy `script.en.md` to `script.<lang>.md` and translate the lines, keeping the numbers.
2. **Record it** as WAVs, pausing between lines. The out-of-character part needs a narrator speaking as themselves. Put your own photo at `assets/author.jpg` and change `authorName`.
3. **Translate the screen text.** Copy `strings.en.js` to `strings.<lang>.js`, translate the `ui` values, and set `lang`.
4. **Transcribe** with `--lang <lang>`, then **align** against your translated script.
5. **Re-point the anchors.** Each one names a word from the English recording; replace it with the word said at that moment in yours. A missing word falls back to the middle of the line and prints a warning in the render log.
6. **Clear the English `captionFixes`** and add any your recording needs.
7. **Build and render** with `--lang <lang>`: `node render.mjs --lang <lang> --preview`.

Keep the tone: dry, warm, jokes on the institution only, and the safety section played straight.

## Tools used

| Tool | Used for |
|---|---|
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (Whisper large-v3) | Word-level transcription, run locally |
| Python + NumPy | Line alignment, cutting, waveform snapping |
| [ffmpeg](https://ffmpeg.org) | Voice clean-up, loudness, encoding, joining |
| Google Chrome via [Playwright](https://playwright.dev) | Drawing each frame |
| HTML, CSS, JavaScript | The composition itself |
| Claude Code | Built the pipeline and scenes with the author, who wrote and voiced the script and reviewed each preview |
