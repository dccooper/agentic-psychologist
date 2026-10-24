# Screen Guide: Antigravity IDE (tutor reference)

<!-- The tutor reads this whenever it gives on-screen directions. Lessons point here instead of describing the screen themselves, so when Antigravity changes, this is the one file to update. -->

- **Last verified:** 2026-10-24, Windows, Antigravity IDE (Standalone), from David's setup screenshots. **Antigravity IDE v2.5.5.**
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

**Open the agent panel** ✅ It's open by default on the right (title **Agent**). Otherwise press **Ctrl+L** (Mac: **Cmd+L** ⚠️), or click **Code with Agent** in the empty editor. ⚠️ The layout icons at the top of the window also toggle the side panels.

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

**Review the AI's changes** ✅ (QA pass 2, Review-driven development). A change shows up in **three places**:
1. **Under the agent's message:** a card, e.g. **1 file changed +20 −1**, with a **Review** button. Review opens the file with the changes highlighted.
2. **In the editor:** added lines are tinted green, removed lines red. Each changed block has its own floating **Accept** (Alt+Enter) / **Reject** (Shift+Alt+Backspace). A bar at the bottom of the editor applies to the whole file: **Accept Changes** (Ctrl+Enter) / **Reject** (Ctrl+Backspace), arrows to jump between changes (Alt+K / Alt+J), and **Edited files 1/2** to move between files.
3. **Above the message box:** **N File(s) With Changes**, listing each pending file with its `+/−` counts, plus **Reject all** / **Accept all**. It stays there until the learner decides, so pending edits from several turns pile up in it.

⚠️ *Inferred, not confirmed:* the change is already written to the file while it's pending (the file on disk showed it), so **Reject** reverts it and **Accept** keeps it. If so, progress saves even before the learner accepts, unless they reject it.

**`progress.md` updates** appear in the same list, so the tutor saves progress only at pause points and lesson ends (see `AGENTS.md`).

**Model** ✅ The model picker sits in the message box. A fresh install (2026-10-24) defaulted to **Gemini 3.8 Flash High**. David has also seen Medium. Before sign-in it shows **No Model Selected**. Learners don't need to change it. ⚠️ Whether the Free plan allows other models is unknown. Never suggest switching models as a fix.

**Voice input** ✅ (icon) / ⚠️ (behavior) A **microphone** icon sits in the message box, next to send. It presumably dictates into the box so you can read and edit before sending. Permission prompts are untested.

**Before sign-in / the start screen** ✅ With no folder open, the editor shows **Open Folder**, **Clone Repository**, recent **Workspaces**, and **Google Extensions** (ignore those). Before sign-in, the agent panel says *"To use the agent, please login here"*, and a blue **Log in →** button sits at the top right.

**Skills in the message box** ✅ Typing `/` plus a skill name turns it into a chip with a small icon (e.g. **start-course**). ✅ *QA pass 3:* type the first few letters (`/meet`) and press **Tab** to fill in the rest. Tell learners this whenever they type a skill name.

**@ and /** ✅ (labels) The message box says *"@ to mention, / for actions"*. **@** attaches a file to your message (Lesson 1.3). **/** runs a command such as `/start-course`. ✅ *QA pass 3:* choosing a file with @ worked. Typing the file's path in the message works as a fallback.

**Settings** ✅ (QA pass 3, Lesson 1.2) The gear menu lists **Open Antigravity IDE User Settings (Ctrl+,)**, **Editor Settings**, **Extensions**, **Keyboard Shortcuts**, and more. ⚠️ Which of these holds the review setting chosen at setup is still unconfirmed.

**Rules and skills (files the learner creates)** ⚠️
- A **rule** is a `.md` file in `.agents/rules/` (Lesson 2.1). ✅ *QA pass 3:* with a rule file open, Antigravity shows an **Activation Mode** setting at the top: **Manual**, **Always On**, **Model Decision**, **Glob**. Use it instead of typing the `trigger:` header (typing both makes a duplicate). A rule with no mode is silently ignored. The file on disk then starts with `---` / `trigger: always_on` / `---`.
- A **skill** is a folder in `.agents/skills/` with a `SKILL.md` inside, starting with `name` and `description` frontmatter (Lesson 2.3).
- Unverified: whether a new rule or skill takes effect in the current conversation or only after **+** (new conversation). Lessons use a new conversation to be safe.

**The terminal** ⚠️ **Terminal → New Terminal** in the top menu, or **Ctrl+`** (Mac: **Ctrl+`** too). It opens as a panel, usually along the bottom. On Windows it's PowerShell by default. `pwd`, `ls`, and `clear` work on both Windows and Mac. The trash-can icon on the panel closes it.

**When the agent wants to run a command** ✅ *QA pass 3:* under **Review-driven development**, Antigravity pops up an approval box even for harmless commands (`python --version`, and `git status --short`, which the agent ran unprompted on `/start-course`). So every command interrupts the learner. `AGENTS.md` now says: no commands before 2.4, and from then on explain each one before running it. ⚠️ The approval box's exact labels aren't captured yet.

## Open items to verify (QA pass 2)

- [x] Google sign-in screens, installer screens, start screen (captured 2026-10-24, in `SETUP.md`)
- [x] Version: Antigravity IDE 2.5.5
- [x] The trust prompt appears when opening the course folder (David, first install). Exact wording not captured
- [x] Typing `/start-course` is recognized as a skill: it turns into a **start-course** chip in the message box (2026-10-24). *Still to confirm:* the tutor then follows the skill correctly.
- [x] Reviewing an AI edit: the Review card, per-change Accept/Reject, the Accept Changes bar, Files With Changes / Accept all (QA pass 2)
- [ ] Whether a pending (unaccepted) edit is already saved to the file, and what Reject does
- [ ] The microphone: dictation vs. voice chat; Windows/Mac permission prompts
- [ ] Exact settings location for the Tab features (Autocomplete, Supercomplete, Tab-to-Jump, Tab-to-Import)
- [ ] Where to change the review setting after setup
- [x] New Folder / New File and typing in Markdown worked (QA pass 2: the learner created `workspace/my-notes/first-week.md` by hand)
- [ ] Free-plan usage limits view, and response times on the default model

**Added for Slice 2 (verify in QA pass 4):**
- [x] The @ file picker works (1.3, QA pass 3)
- [x] Rules have an **Activation Mode** toggle (Manual / Always On / Model Decision / Glob); an Always On rule was followed in a new conversation (2.1, QA pass 3)
- [ ] Whether the Activation Mode toggle writes the `trigger:` header to disk itself
- [x] A new skill runs from `/` in a new conversation, and Tab completes the name (2.3, QA pass 3)
- [ ] Whether a new skill works in the *same* conversation it was created in
- [x] Opening the terminal worked in 2.4 (QA pass 3, no issues reported). Which of the two ways the tester used isn't recorded.
- [x] Review-driven development asks before every command, including `python --version` (2.4, QA pass 3)
- [ ] The approval box's exact labels (screenshot)
