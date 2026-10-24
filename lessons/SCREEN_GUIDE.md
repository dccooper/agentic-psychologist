# Screen Guide: Antigravity IDE (tutor reference)

<!-- The tutor reads this whenever it gives on-screen directions. Lessons point here instead of describing the screen themselves, so when Antigravity changes, this is the one file to update. -->

- **Last verified:** 2026-10-24, Windows, Antigravity IDE (Standalone), from David's setup screenshots. Version not recorded (the download page listed v2.5.5). Record it next time (Help → About).
- **Status key:** ✅ seen in a test screenshot · ⚠️ inferred (usually from standard VS Code behavior; Antigravity is built on VS Code), not yet confirmed
- **Setup** (download, Google sign-in, first-run screens) is in `SETUP.md`. Learners do it before the tutor exists.

## The rule for giving directions

**Name things by their label first.** Say "open the **Explorer**," then add where it usually is ("the list of files, usually on the left") as a hint. Panels can be moved or hidden. If what the learner sees doesn't match, ask them to describe their screen and adapt.

## The window ✅

| Area | How to recognize it | What it's for |
|---|---|---|
| **Explorer** | Heading **EXPLORER**, the course folder's name, then folders: `data`, `docs`, `lessons`, `planning`, `QA`, `workspace`, `world` … Usually on the left. | Finding and opening files |
| **Activity bar** | A thin strip of icons along the edge of the window. The top icon (stacked pages) opens the Explorer. Others: Search, Source Control, Run, Extensions. | Switching what the side panel shows |
| **Editor** | The large middle area. With nothing open it shows **Antigravity IDE — Code with Agent (Ctrl+L)**. Open files appear here as tabs. | Reading and editing files |
| **Agent panel** | The conversation title at the top (e.g. "Start Course"), with **+** (new conversation), a clock icon (history), **…** and **×**. The message box at the bottom says *"Ask anything, @ to mention, / for actions"*. Usually on the right. | Talking to the tutor |
| **Status bar** | The thin bar at the very bottom (e.g. `main*`, `0 ⚠ 0`, **Antigravity - Settings**) | Ignore it for now |

While the agent works, the agent panel shows its activity (e.g. *"Exploring 1 file, 1 folder"*, *"Analyzed README.md"*, *"Working…"*). Replies can take several seconds on the default model.

## Common actions

**Open the agent panel** ✅ **Ctrl+L** (Mac: **Cmd+L** ⚠️), or click **Code with Agent** in the empty editor. ⚠️ The layout icons at the top of the window also toggle the side panels.

**Start a fresh conversation** ✅ The **+** at the top of the agent panel. ⚠️ Course progress lives in `workspace/progress.md`, so a new conversation loses nothing. Type `/start-course` to resume.

**Open a file** ✅ (Explorer) / ⚠️ (click to open)
1. Open the **Explorer** (top icon in the activity bar, or **Ctrl+Shift+E** ⚠️).
2. Click a folder to expand it, e.g. `world`, then `artifacts`.
3. Click the file. It opens as a tab in the editor.

**Markdown files** ⚠️
`.md` files open as **plain text you can type in** (the `#`, `-` and `**` symbols are visible). To see the formatted version, right-click the file's tab or name and choose **Open Preview**, or press **Ctrl+Shift+V**.

**Make a folder or file** ⚠️
In the Explorer, right-click the folder you want it in (e.g. `workspace`) and choose **New Folder…** or **New File…**, then type the name and press **Enter**. Hovering over the Explorer heading also shows small new-file and new-folder icons.

**Save** ⚠️ **Ctrl+S** (Mac: **Cmd+S**). A dot on a file's tab means it has unsaved changes.

**How much the agent may do on its own** ✅ (labels from setup) / ⚠️ (behavior)
During setup the learner chose one of: **Strict Mode**, **Review-driven development** (*Recommended*; what `SETUP.md` tells learners to choose), **Agent-driven development** (*"The agent will never request for review"*), or **Custom configuration**. ⚠️ Where to change it later is unknown, probably **Antigravity - Settings** (status bar) or the gear icon. This matters for Lesson 1.1 (reviewing changes) and 1.2 (deciding how much the AI may do alone).

**Review the AI's changes** ⚠️ *Not yet observed. Top priority for QA pass 2.*
Under Review-driven development, the agent should ask before applying changes, and edited files should show the changes for you to accept or reject. Until verified, ask the learner to describe what appears after the AI edits a file (in the agent panel and in the editor), and to read out the button names. Record what they say in `progress.md` Notes.

**Model** ✅ The model picker sits in the message box (e.g. **Gemini 3.8 Flash High**). The default is **Gemini 3.8 Flash (Medium)**. Learners don't need to change it. ⚠️ Whether the Free plan allows other models is unknown. Never suggest switching models as a fix.

**@ and /** ✅ (labels) The message box says *"@ to mention, / for actions"*. **@** attaches a file to your message (Lesson 1.3). **/** runs a command such as `/start-course`.

## Open items to verify (QA pass 2)

- [ ] Antigravity version (Help → About), plus the Google sign-in screens (screenshots for `SETUP.md`)
- [ ] Whether the trust prompt appears when opening the course folder
- [ ] Whether typing `/start-course` runs the skill, or only works through the `AGENTS.md` backstop
- [ ] **What reviewing an AI edit looks like** under Review-driven development (exact button labels)
- [ ] Where to change the review setting after setup
- [ ] New Folder / New File by right-click; Markdown opens as editable text
- [ ] Free-plan usage limits view, and response times on the default model
