# Agent Fix Plan (Draft)

## QA-001 — Correct file-navigation guidance in Course initiation Step 2
- **Priority:** Medium
- **Problem:** Step 2 incorrectly says the file list is on the left in the observed Cursor layout.
- **Proposed fix:** Update the tutor's navigation language to instruct the learner to click **Files** on the right, select **Browse Files** if necessary, then open `world/artifacts/welcome-email.md`. Make wording resilient to UI layout differences where possible.
- **Acceptance criteria:** Navigation starts from the Files entry point; Browse Files is explicitly covered; the path is correct; identifying the email sender remains the checkpoint; no claim that the file explorer is already visible.
- **Evidence:** [Before](screenshots/issue-001-before.png) · [After](screenshots/issue-001-after.png)
- **Verification:** Run course initiation Step 2 in the default Cursor UI and confirm the user can follow the instructions.
- **Status:** fixed, needs retest (see resolution.md)

## QA-002 — Correct sender identification and validation in Course initiation Step 2
- **Priority:** Medium
- **Problem:** The tutor changes the sender's surname from **Okafor** (source email) to **Okonkwo**, then dismisses the mismatch as an acceptable spelling difference.
- **Proposed fix:** Ground the checkpoint's answer in `world/artifacts/welcome-email.md`, with **Dr. Miriam Okafor** as the expected sender. Do not assert an alternate identity or excuse a name discrepancy without source support. Check any lesson scripts, answer keys, or evaluation instructions for the wrong surname.
- **Acceptance criteria:** A reply identifying “Dr. Miriam Okafor” is accepted; the tutor repeats the correct name if it repeats a name at all; it does not invent an alternative spelling or person; the lesson proceeds to reading/question formation.
- **Evidence:** [Screenshot](screenshots/issue-002-name-mismatch.png)
- **Verification:** Repeat sender checkpoint with the source file visible; check the assistant's response against both sender line and signature.
- **Status:** fixed, needs retest (see resolution.md)

---

# Instructional Improvements (Not Bugs)

## NOTE-001 — Make the learning objective explicit after document Q&A
- **Scope:** Course initiation, after the learner asks a question about the welcome email and receives an answer; generalize across subsequent lessons.
- **What to retain:** Keep the welcome-email exercise as the opening activity.
- **Recommendation:** Insert a brief retrospective teaching moment that names the skill: using an LLM to read a document and distill relevant information via a plain-language question. For later exercises, explicitly draw out the transferable lesson after the learner completes the task.
- **Possible tutor wording:** “What you just did is a core way to use an AI assistant: give it a document, ask a question in your own words, and have it pull out the information you need. You didn't have to manually search the document or phrase the question in any special way.”
- **Acceptance criteria:** The lesson remains interactive; the tutor explains the practical capability after the Q&A (not before); takeaway is concise, specific to the task, and memorable; similar takeaways recur where appropriate throughout the course.
- **Status:** suggested enhancement; not an error

## QA-003 — Make saving progress and Cursor mode selection actionable
- **Priority:** Medium
- **Problem:** Tutor instructs a novice learner to “Switch to Agent mode” even though the visible dropdown only contains Plan, Debug, Multitask and Ask, without telling them how to return to the file-editing chat or save course progress.
- **Proposed fix:** Verify the mode picker on the supported Cursor version; give exact UI steps to exit Ask mode and access a file-editing-capable mode. Explicitly direct the tutor to update `workspace/progress.md` after the switch, or provide a manual fallback. Clarify that mode switching does not itself persist a previous lesson's completion.
- **Acceptance criteria:** Learner can follow the instructions on the tested UI without guessing; tutor accurately describes Ask's read-only restriction; progress remains consistent with actual lesson completion; completion persists in `workspace/progress.md` once write access is available; no unsupported claim that Agent mode is absent.
- **Evidence:** [Mode picker screenshot](screenshots/issue-003-mode-picker.png)
- **Verification:** Reproduce after lesson 0.1 in Ask mode; follow the corrected directions, open `workspace/progress.md`, and verify lesson 0.1 changes to completed. Reopen the course to confirm persistence.
- **Status:** fixed, needs retest (see resolution.md)

## NOTE-002 — Reframe “Can I paste this?” as an IT Security onboarding email
- **Scope:** Lesson 0.2, source artifact for the eight-scenario data-handling exercise.
- **What to retain:** All eight scenario prompts, their distinct risk factors, and the learner's task to classify each OK / NOT OK / IT DEPENDS and explain why.
- **Recommendation:** Change the presentation from an informal message by Jordan to a realistic onboarding compliance email from an IT Security or Privacy/Compliance team, with From/To/Subject fields, a concise policy-oriented introduction, clear exercise instructions, and a professional but accessible tone. Keep the fictional training context evident. Make the artifact consistent with the welcome email's document-based learning workflow.
- **Acceptance criteria:** Looks and reads like a plausible IT Security onboarding email; preserves the educational exercise and scenario distinctions; does not reveal correct answers prematurely; tutor invites learner to assess and explain answers before teaching the generalizable privacy/compliance lesson.
- **Evidence:** [Current artifact screenshot](screenshots/note-002-compliance-exercise.png)
- **Status:** suggested enhancement; not an error

## QA-004 — Rework Lesson 1.1 to match observed Cursor UI
- **Priority:** Medium (repeat of a common UI-assumption pattern)
- **Problem:** Lesson 1.1 explicitly calls the file panel the left-side panel and the editor the middle, while the observed UI has the chat/repositories sidebar on the left, the open file/editor on the right, and the Files tree to the far right.
- **Proposed fix:** Audit and rewrite `Lesson 1.1 — Finding your way around Cursor` to identify regions by their purpose and visible labels, with real instructions for opening the Files view if hidden. Avoid universal positional claims. Use screenshot-backed examples showing the supported default configuration; mention layouts can be rearranged.
- **Acceptance criteria:** A beginner can identify chat, open editor and file explorer on the screenshot; instructions are accurate for the supported Cursor build; the course gives a recovery path for hidden panels; no false left/middle/right assumptions are made.
- **Evidence:** [Observed lesson and UI](screenshots/issue-004-cursor-layout.png)
- **Verification:** Run lesson 1.1 on a clean/default UI state and on a state with the Files tree shown; compare descriptions to screenshot references.
- **Status:** fixed, needs retest (see resolution.md)

## NOTE-003 — Screenshot-backed UI instruction regression suite
- **Scope:** Every lesson with Cursor-specific screen, menu, click, mode, or file-navigation instructions.
- **Recommendation:** Build a lesson-to-screen inventory and a repeatable comparison workflow. Store each screenshot with tested Cursor version, platform, date, viewport, and state (panels opened/closed). Cross-check every UI-dependent instruction against visible controls. Flag unsupported labels, assumed panel locations, missing steps, mode names and impossible actions. Maintain explicit human confirmation for ambiguous visual differences.
- **Automation:** Add (1) static lint for brittle UI phrases and expected file paths; (2) optionally screenshot-based comparison using a vision-capable model that reports evidence, confidence and uncertainty; (3) manual acceptance passes on updated Cursor versions. Pixel-perfect image diffs alone are insufficient because panels resize and themes change.
- **Acceptance criteria:** Every UI-dependent lesson step has a recorded test case and reference screenshot/state; mismatches produce issues with exact wording and evidence; the suite is rerun after Cursor/course updates; ambiguous assertions are not auto-declared failures without review.
- **Implementation starter:** [tests/README.md](tests/README.md) and [tests/ui-instruction-matrix.md](tests/ui-instruction-matrix.md).
- **Status:** proposed enhancement / not an error

## NOTE-004 — Expand the Markdown introduction in Lesson 1.1
- **Scope:** Lesson 1.1, immediately after the instruction to create `workspace/my-notes/first-week.md` and add a heading and sentence.
- **Recommendation:** Add a brief, beginner-friendly explanation of Markdown as a plain-text format with simple formatting symbols; explain why AI coding agents use `.md` files for instructions, notes, plans, and documentation (readable to people and tools; easily editable and diffable). Demonstrate only the syntax already relevant to the exercise (`# My First Week` plus optional bullets). Offer an optional link to [Markdown Guide — Basic Syntax](https://www.markdownguide.org/basic-syntax/) or [CommonMark Help](https://commonmark.org/help/), without turning it into a separate mandatory lesson.
- **Possible tutor wording:** “The `.md` ending means Markdown. It’s ordinary text with a few simple formatting shortcuts: `#` makes a heading and `-` starts a list. Agents often use Markdown for notes, plans, instructions, and documentation because people and AI tools can read and update it easily. You only need a couple of symbols to get started; here's a [quick syntax reference](https://www.markdownguide.org/basic-syntax/) if you want more.”
- **Acceptance criteria:** The learner can state what `.md` means and give a basic example; can describe at least one reason agents use Markdown; receives an optional trustworthy syntax resource; instruction remains concise and placed at the point of use.
- **Evidence:** [Lesson screenshot](screenshots/note-004-markdown-intro.png)
- **Status:** suggested enhancement / not an error

## QA-005 — Teach the actual file-change review workflow in Lesson 1.1
- **Priority:** Medium
- **Problem:** Tutor skips the visible **Review** entry point while instructing novice learners to accept/reject an AI edit. The change summary includes `first-week.md` and `progress.md`, but the lesson focuses only on the former.
- **Proposed fix:** Rewrite this checkpoint as: locate **2 Files Changed**, click **Review**, inspect the proposed changes to `first-week.md` (additions/deletions), compare against the original heading/feeling line and Jordan's guide, then accept or reject the proposed edits using the controls actually shown in the review view. Separately explain the `progress.md` change, which may need independent review. Avoid depending on green/red alone (accessibility and theme variation).
- **Candidate learner language:** “You should see a **2 Files Changed** card at the bottom of the chat. Click **Review**. Start with `first-week.md`. Check that your heading and feelings sentence are still there, then read the proposed checklist for missing details or invented items. The added/removed line counts summarize the changes; inspect the actual diff before deciding. You may also see `progress.md`, which is the course progress file—review that separately. Choose whether to keep or reject changes using the options shown in the review panel, and tell me what you chose.”
- **Acceptance criteria:** Instructions name the visible Review control and both files in the changes card; accurately guide the learner into the review experience; do not assume controls not verified by the supported Cursor version; prompt a deliberate decision before proceeding; screenshot regression test passes.
- **Evidence:** [Screenshot](screenshots/issue-005-review-changes.png)
- **Verification:** Capture the UI after clicking Review, verify exact accept/reject wording and any per-file vs all-files behavior; retest with a modified `first-week.md` and `progress.md`.
- **Status:** fixed, needs retest (see resolution.md)
