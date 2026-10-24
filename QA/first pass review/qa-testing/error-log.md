# QA Error Log

## Issue QA-001

### 2026-10-23 · Course initiation · Step 2 — Open the welcome email
- **Type:** broken step | confusing wording
- **Severity:** Medium
- **What happened:** Tutor says that the file list is on the left. In the observed default Cursor layout, the left sidebar instead shows repositories/chat navigation; the Files entry point is on the right. The user must open Files, then Browse Files, then navigate to the requested file.
- **Expected:** Give navigation instructions aligned with the observed layout: Files → Browse Files → world → artifacts → welcome-email.md. Preserve checkpoint asking the user who sent the email.
- **Exact error text:** “On the left, the file list works like a filing cabinet. Open these in order:”
- **Error text / screenshot:** [Before — initial layout](screenshots/issue-001-before.png); [After — file open](screenshots/issue-001-after.png)
- **Status:** fixed, needs retest (see resolution.md)
- **Notes:** This is a UI instruction mismatch, not evidence that the file is missing. Adapt instructions if Cursor layouts vary.

## Issue QA-002

### 2026-10-23 · Course initiation · Step 2 — Welcome email sender checkpoint
- **Type:** tutor went off-script | factual error | incorrect validation
- **Severity:** Medium
- **What happened:** The user correctly identified the sender of `world/artifacts/welcome-email.md` as Dr. Miriam Okafor. The tutor replied that the email was from “Dr. Miriam Okonkwo” and said the file might show a slightly different spelling and that either way the correct document had been opened. The source email shows “Dr. Miriam Okafor” in its sender line and signature.
- **Expected:** Recognize “Dr. Miriam Okafor” as the correct sender, without changing the surname. Validate the user's answer against the actual file rather than excusing discrepancies in a factual checkpoint.
- **Exact error text:** “Good — that’s the checkpoint. The email is from Dr. Miriam Okonkwo (the file may show a slightly different spelling; either way, you’ve got the right document).”
- **Error text / screenshot:** [Tutor response and source email](screenshots/issue-002-name-mismatch.png)
- **Status:** fixed, needs retest (see resolution.md)
- **Notes:** Suspected cause is not established. Check whether the expected name is hard-coded in lesson instructions or generated without grounding in the source file.

---

# Course Improvement Notes (Not Errors)

## NOTE-001

### 2026-10-23 · Course initiation · After welcome email question
- **Type:** instructional emphasis | learning objective clarity
- **What works:** Beginning with a learner asking the LLM a question about a real document is a good introductory exercise.
- **Opportunity:** After the learner asks about the email in their own words and the tutor answers, explicitly articulate what they just accomplished: giving an LLM a document, having it read the contents, and distilling useful information in response to a natural-language question.
- **Expected:** Add a short, clear takeaway at the end of this activity. Extend this instructional pattern throughout the course: explain the core skill or lesson learned after each exercise instead of leaving it implicit.
- **Status:** suggestion / not an error

## Issue QA-003

### 2026-10-23 · Course initiation → Lesson 0.2 transition · Saving progress
- **Type:** confusing wording | Cursor/tool instruction error
- **Severity:** Medium
- **What happened:** After completing lesson 0.1, tutor says `progress.md` remains “not started” because Ask mode cannot write files, then instructs the learner to “Switch to Agent mode.” The mode picker shown in the screenshot offers Plan, Debug, Multitask and Ask, but does not visibly list Agent. The learner cannot infer what to click or whether ordinary (non-specialized) chat is already Agent mode.
- **Expected:** Explain, using the current Cursor UI, how to enter a file-editing-capable chat mode, verify that the chat has editing ability, and explicitly request/update `workspace/progress.md`. Do not suggest simply switching modes saves progress automatically. If Ask mode is intended for the intro, provide a reliable alternate progress-recording method.
- **Exact error text:** “Lesson 0.1 is done (name, email opened, question asked). `progress.md` still says ‘not started’ because this chat is in Ask mode and can’t write files. Switch to Agent mode when you want that saved.”
- **Error text / screenshot:** [Mode menu showing Plan, Debug, Multitask, Ask](screenshots/issue-003-mode-picker.png)
- **Status:** fixed, needs retest (see resolution.md)
- **Notes:** Official Cursor documentation differentiates read-only Ask from file-editing Agent. The actual UI pathway and whether the unlabeled default is Agent remain to be verified for the installed version; avoid treating that interpretation as established fact. Also consider whether splitting modes is an appropriate novice onboarding experience.

## NOTE-002

### 2026-10-23 · Lesson 0.2 — “Can I paste this?” compliance exercise
- **Type:** instructional improvement | artifact framing
- **What works:** The eight scenarios are a useful practical test of what can and cannot be entered into an AI tool, especially for clinical or research information.
- **Opportunity:** The current `Can I paste this? (from Jordan)` artifact reads like an informal note from a peer. Make it resemble the kind of formal but approachable security-awareness / compliance email that a new employee might receive from IT Security during onboarding, similar to the opening welcome email artifact.
- **Expected:** Retain the eight cases and the OK / NOT OK / IT DEPENDS classification with explanations. Reframe with a believable sender, recipient, subject, brief company-compliance context, and instructions for the exercise. Avoid giving away answers before the learner responds.
- **Error text / screenshot:** [Current exercise](screenshots/note-002-compliance-exercise.png)
- **Status:** suggested enhancement / not an error

## Issue QA-004

### 2026-10-23 · Lesson 1.1 — Finding your way around Cursor
- **Type:** broken step | outdated UI instructions | confusing wording
- **Severity:** Medium
- **What happened:** Lesson describes the three Cursor areas as "File panel — left side", "Editor — middle", and "Chat — where you and I are talking." The observed screenshot shows chat and repositories on the left, an open document/editor in the right-hand area, and a file tree docked on the far right. Learner is asked to identify panels based on a layout that contradicts the reference screenshot.
- **Expected:** Give navigation guidance consistent with the supported Cursor UI; teach the identity and purpose of the chat, editor, and Files explorer using controls and labels, while acknowledging movable/hidden panels. If a file pane must be exposed, give actionable steps.
- **Exact error text:** “File panel — left side, the list of folders and files.” / “Editor — middle, where an open file’s text shows.”
- **Error text / screenshot:** [Lesson 1.1 and observed layout](screenshots/issue-004-cursor-layout.png)
- **Status:** fixed, needs retest (see resolution.md)
- **Notes:** This is distinct from QA-001 (intro Step 2); evaluate shared root cause / repeated spatial assumptions across all lessons.

## NOTE-003

### 2026-10-23 · Cross-course — Screenshot-backed UI instruction tests
- **Type:** QA / regression-testing improvement | test infrastructure
- **Opportunity:** Navigation guidance may become stale as Cursor changes its menus, panel placement, and default modes. Current QA-001, QA-003 and QA-004 show repeated UI assumptions.
- **Expected:** Introduce a repeatable cross-course UI instruction review, using versioned screenshots as evidence and a checklist of UI-dependent claims from each lesson. Automate exact-label/path checks where practical; reserve visual/semantic interpretation for human review or an image-capable model, with uncertain findings marked for confirmation. Recheck following Cursor updates and lesson edits.
- **Evidence:** [Observed layout](screenshots/issue-004-cursor-layout.png); [Initial layout](screenshots/issue-001-before.png); [Mode picker](screenshots/issue-003-mode-picker.png)
- **Status:** proposed enhancement / not an error

## NOTE-004

### 2026-10-23 · Lesson 1.1 — Creating `first-week.md` in `workspace/my-notes`
- **Type:** instructional improvement | foundational concept explanation
- **What works:** Learner creates a Markdown file (`first-week.md`) and writes a heading, giving a concrete hands-on first experience.
- **Opportunity:** Tutor explains `.md` only briefly (“Markdown — plain text with a few symbols for headings and lists”; “files are just text”), without explaining what Markdown is in practical terms, why AI coding agents use it, or where to learn basic syntax.
- **Expected:** Add a short just-in-time explanation after or alongside the file-creation step: Markdown is a plain-text format that uses lightweight markers (`#` headings, `-` lists, `**bold**`, `[text](url)` links). Explain why it is helpful with AI agents: human-readable, easy to edit and version-control, and commonly used for agent instructions, plans, notes, and documentation. Provide a reputable optional syntax reference (e.g., https://www.markdownguide.org/basic-syntax/ or https://commonmark.org/help/). Keep the exercise focused: avoid forcing a lengthy Markdown tutorial before completing the task.
- **Error text / screenshot:** [Tutor explanation of Markdown](screenshots/note-004-markdown-intro.png)
- **Status:** suggested enhancement / not an error

## Issue QA-005

### 2026-10-24 · Lesson 1.1 — Review proposed AI file edits
- **Type:** confusing wording | incomplete Cursor UI instructions
- **Severity:** Medium
- **What happened:** After editing `first-week.md`, the tutor says changes show as additions/deletions (often green/red), tells the learner to inspect the file, then to "accept (or reject and ask me to try again)." The observed UI shows a **2 Files Changed** card listing `first-week.md` (+25 −1), `progress.md` (+1 −1), and a **Review** control. The tutor does not say to click Review, nor distinguish the lesson file from the unrelated progress update. The screenshot does not show the controls that appear *after* clicking Review, so their labels and placement are not yet verified.
- **Expected:** First direct the learner to the visible **2 Files Changed → Review** UI; then have them review the `first-week.md` diff, confirm their heading and feeling line survived, check for missing/invented checklist items, and use the accept/reject controls *as labeled in the opened review interface*. Explain that `progress.md` is a separate file change, and what to do with it. Avoid assuming diff colors alone explain the workflow.
- **Exact error text:** “Before you accept, look at the file and check ... Then accept (or reject and ask me to try again). Tell me what you decided.”
- **Error text / screenshot:** [Tutor explanation and two-files-changed review card](screenshots/issue-005-review-changes.png)
- **Status:** fixed, needs retest (see resolution.md)
- **Notes:** Verify actual post-Review interface using a second screenshot or live interaction before hard-coding acceptance control names.
