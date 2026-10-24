# Cursor UI Map (tutor reference)

<!-- Read by the tutor whenever it gives directions on screen. Lessons point here instead of describing the screen themselves, so when Cursor changes, this is the one file to update. -->

- **Last verified:** 2026-10-23, Windows, Cursor's **Agents window** layout (QA pass 1). Cursor version not recorded. Record it next time (Help → About).
- **Status key:** ✅ seen in a test screenshot · ⚠️ inferred, not yet confirmed

## The rule for giving directions

**Name things by their label, not their position.** Say "click **Files**," not "look on the left." Layouts differ between Cursor versions and between the two layouts below, and panels can be moved or hidden. If what the learner sees doesn't match, ask them to describe their screen and adapt.

## Two layouts

Cursor has two layouts. Learners may land in either one.

1. **Agents window** ✅ (what the first tester saw). The chat sits in the main area. There's a button labeled **IDE ↗** above the chat.
2. **IDE (classic editor)** ⚠️. The **IDE ↗** button opens it. A file explorer sits along one side, open files sit in the middle, and the chat sits in a side panel.

The directions below are for the **Agents window**. If the learner is in the IDE layout, the same ideas apply, but the controls are in different places. Ask what they see.

## Areas of the Agents window ✅

| Area | How to recognize it | What it's for |
|---|---|---|
| **Sidebar** | **New Chat**, **Search**, and a **Repositories** list with the course folder (e.g. `aug_psych`) and its chats underneath | Starting a new chat; returning to an old one |
| **Chat** | The conversation, with a message box at the bottom that says "Ask questions" or "Send follow-up" | Talking to the tutor |
| **Project panel** | **Open Tabs**, then, under the course folder's name, **Changes**, **Browser**, **Terminal**, **Files**. If it's hidden, use the panel-toggle icon at the top corner of the window | Getting to files and changes |
| **File viewer** | Opens when a file is clicked. A path at the top (e.g. `world > artifacts > welcome-email.md`) and **Preview** / **Source** buttons | Reading and editing files |
| **Files tree** | The list of the course's folders: `.cursor`, `data`, `docs`, `lessons`, `planning`, `workspace`, `world` … | Finding and opening files |

## Common actions

**Open a file** ✅
1. Click **Files** in the project panel (choose **Browse Files** if it appears).
2. In the Files tree, click folders to open them, e.g. `world`, then `artifacts`.
3. Click the file. It opens in the file viewer.

**Edit a file by hand** ⚠️
Markdown files open in **Preview** (formatted, like a document). To type in one, click **Source**.

**Make a folder or file** ⚠️
Right-click a folder in the Files tree and look for **New Folder** / **New File**. If those options aren't there, have the learner describe what they see. The fallback is the **IDE ↗** layout, which has them.

**Chat modes** ✅ (labels seen) / ⚠️ (meaning inferred)
- The mode shows as a small tag **inside the message box**, e.g. a green **Ask ×** tag.
- **No tag = the default mode, which can read *and* edit files.** This is what the course needs nearly all the time. (Cursor's docs call it Agent mode, but the menu doesn't list "Agent." It's simply the default.)
- **Ask** = read-only. The AI can read files but **can't change them**, so progress can't be saved. To leave Ask, click the **×** on the tag.
- The mode menu lists **Plan**, **Debug**, **Multitask**, and **Ask**.
- Never tell a learner to "switch to Agent mode." Tell them to **remove the Ask tag** (click its ×).

**Review AI changes** ✅ (card) / ⚠️ (inside Review)
- After the AI edits files, a card appears under its message: **"N Files Changed"**, with each file listed with `+added −removed` line counts and a **Review** button.
- Click **Review** to see the actual changes, then keep or undo them with the buttons shown. *The labels inside Review are not yet verified.* Ask the learner to read them out the first time.
- `progress.md` often appears in this list too. That's the tutor updating the course bookmark. It's fine to keep.
- There's also a **Changes** item in the project panel and a **Changes +N −N** button above the message box. They lead to the same changes.
- Ignore **Create Branch & Commit** until Graduation (G.1).

**Model** ✅
The model name shows in the message box (e.g. "Cursor Grok 4.6 Medium"). **On the Free plan it's locked to that model.** Choosing a different one requires a paid plan. So never tell a learner to "switch models" as a fix. Testers should record it.

## Open items to verify (next test)

- [ ] Cursor version number and whether a **fresh install** opens in the Agents window or the IDE layout
- [ ] The buttons inside **Review** (exact labels; per file or all at once)
- [ ] Making a folder and a file by hand in the Agents window
- [ ] Whether a fresh chat starts with no mode tag (i.e., can edit files)
- [ ] Whether Preview allows typing, or Source is required
