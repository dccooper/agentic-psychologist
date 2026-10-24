# Resolution: QA Pass 1 (Slice 1)

Fixed 2026-10-24. **All items need a retest in Cursor.** Nothing below has been verified live yet.

## Root causes

1. **Wrong layout assumed.** The lessons were written for the classic IDE layout (files on the left, editor in the middle). The tester's Cursor opened in the **Agents window** (chat in the main area; Files, Changes, Browser, and Terminal in a project panel). → QA-001, QA-004, QA-005.
2. **The session ran in Ask mode** (read-only), so the tutor couldn't save progress, and the lesson continued anyway. "Agent" isn't listed in the mode menu, because it's the default (no tag). → QA-003.
3. **The tutor answered from memory instead of reading the file.** The learner typed "Okefor" (a typo). The tutor "corrected" it to an invented name, "Okonkwo." The model was Cursor Grok 4.6 Medium. → QA-002.

## Fixes

| Item | Fix | Files |
|---|---|---|
| **Shared** | New **UI map**: one file with all on-screen directions, by label, marked ✅ verified / ⚠️ inferred. Lessons point to it, so when Cursor changes, only it needs updating. Tutor rule: directions by label, never by position. | `lessons/CURSOR_UI.md`, `.cursor/rules/tutor.mdc`, `.cursor/skills/im-stuck/SKILL.md` |
| QA-001 | 0.1 step 2: **Files** → (Browse Files) → world → artifacts → welcome-email.md. Sticking point for a hidden panel. | `lessons/0-getting-started/0.1-welcome.md` |
| QA-002 | 0.1 checkpoint now states the **expected answer (Dr. Miriam Okafor)**, accepts typos, and never offers a different name. New tutor rule: *check answers against the file, never from memory.* `/next-step` reads the file for content checkpoints. The template now asks for expected answers. | `0.1-welcome.md`, `tutor.mdc`, `next-step/SKILL.md`, `LESSON_TEMPLATE.md` |
| QA-003 | `/start-course` checks first that it can edit files. If it's in Ask mode, it tells the learner to **click the × on the Ask tag** and stops. The tutor never says "switch to Agent mode." The README quick start says the same. The 1.2 outline notes the actual mode menu. | `start-course/SKILL.md`, `tutor.mdc`, `README.md`, `lessons/OUTLINE.md` |
| QA-004 | 1.1 rewritten: the areas are named by purpose and label (chat / Files / file viewer); New Folder via right-click with a fallback; a Preview vs. Source tip. | `lessons/1-foundations/1.1-finding-your-way.md` |
| QA-005 | 1.1 step 6 walks through **N Files Changed → Review** one step at a time. The learner reads out the buttons inside Review (this verifies the UI map). The tutor updates `progress.md` *after* the review, so the card shows only their file, and explains `progress.md` if it appears. | `1.1-finding-your-way.md`, `CURSOR_UI.md` |
| NOTE-001 | Tutor rule: **name the takeaway** after every exercise. 0.1's takeaway reworded to your suggested wording and marked "don't skip." Added a takeaway to 0.2. The template has a "Name the moment" final step. | `tutor.mdc`, `0.1`, `0.2`, `LESSON_TEMPLATE.md` |
| NOTE-002 | `can-i-paste-this.md` is now a formal email from the Office of Research Compliance (Ward, Locke & Key), with From/To/Subject, why it matters, and instructions. The 8 scenarios are unchanged, with no answers. One gag. | `world/artifacts/can-i-paste-this.md`, `0.2-what-never-goes-in.md` |
| NOTE-003 | Lightweight version: every lesson gets a **"UI this lesson depends on"** list (the regression checklist), backed by the UI map's verified/inferred markers and an "open items to verify" list. The testing protocol now records the Cursor version, layout, and model. *Not built:* automated lint or vision checks (revisit if the lesson count makes manual rechecks painful). | `LESSON_TEMPLATE.md`, lessons 0.1/0.2/1.1, `planning/PLAN.md` §10–11 |
| NOTE-004 | 1.1 step 3: a just-in-time Markdown explanation (what it is, why agents use it, a markdownguide.org link), given *after* they type, three sentences max. | `1.1-finding-your-way.md` |

## To verify on retest

From `lessons/CURSOR_UI.md` → "Open items to verify":
- Cursor version (Help → About). **Your build showed "stops working at the end of November." Update first.**
- Whether a fresh install opens in the Agents window or the IDE layout
- The button labels inside **Review**
- New Folder / New File by right-click in the Agents window
- Whether a fresh chat starts with no mode tag
- Whether typing works in Preview or needs Source
