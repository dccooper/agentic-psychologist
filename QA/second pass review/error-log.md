# QA Error Log and Instructional Notes — Vertical Slice 2

**IDE:** Antigravity
**Started:** 2026-10-24
**Scope:** New vertical-slice retest; independent of Cursor Vertical Slice 1.

## Bugs

_No bugs recorded yet._

<!-- Template:
### YYYY-MM-DD · Lesson / section · step
- **ID:** QA-001
- **IDE:** Antigravity
- **Type:** tutor went off-script | broken step | confusing wording | IDE/tool error | cost (request count)
- **Severity:** low | medium | high
- **What happened:**
- **Expected:**
- **Error text / screenshot:** screenshots/issue-001.png
- **Status:** open
-->

## Instructional improvements

### 2026-10-24 · Course initiation / early lessons · Reviewing AI file edits
- **ID:** NOTE-001
- **IDE:** Antigravity
- **Type:** instructional improvement | review workflow | learner friction
- **What works:** Antigravity shows proposed changes in the editor as a diff, with options to accept or reject individual changes and an **Accept all** control. This creates a natural opportunity to teach learners to review what an AI agent changes.
- **Opportunity:** Requiring manual approval of every routine edit throughout the course may become repetitive or irritating. However, encouraging blanket acceptance too early may undermine the intended lesson about inspecting AI work.
- **Expected:** Teach explicit review and approval in the first exercises; later introduce when accepting a batch of reviewed changes is appropriate, while retaining review for consequential, unexpected, or sensitive edits. Distinguish *Accept all proposed changes* from *automatically approving future changes*—they are not equivalent.
- **Evidence:** `screenshots/note-001-change-approval.png` (proposed changes to `workspace/progress.md`, editor diff, per-change accept/reject and **Accept all** controls).
- **Status:** suggested enhancement
- **Follow-up observation (2026-10-24):** A subsequent screenshot shows `progress.md` listed in a **1 File With Changes** card directly above the Antigravity chat composer, with **Reject all** and **Accept all** controls. This suggests routine course-progress updates may repeatedly surface as pending approvals in the chat area; frequency and whether the card always appears have not yet been verified.
- **Additional evidence:** `screenshots/note-001-progress-change-card.png`.
- **Additional recommendation:** Explicitly teach what this persistent-looking change card means, distinguish the chat card from the editor diff, and avoid making progress bookkeeping a recurring distraction. Validate whether learners must approve each `progress.md` update before relying on its saved state; do not suppress review or auto-approve without an intentional risk-based design decision.


<!-- Template:
### YYYY-MM-DD · Lesson / section · step
- **ID:** NOTE-001
- **Type:** instructional improvement
- **What works:**
- **Opportunity:**
- **Expected:**
- **Screenshot:** screenshots/note-001.png
- **Status:** suggested enhancement
-->

### 2026-10-24 · Course initiation / early lessons · Introduce voice input
- **ID:** NOTE-002
- **IDE:** Antigravity
- **Type:** instructional improvement | onboarding | input modality
- **What works:** Antigravity offers a microphone control in the chat composer, providing an alternative to typing.
- **Opportunity:** The course currently does not explicitly encourage learners to try voice input early. Dictation may lower typing friction, especially for natural-language prompts.
- **Expected:** Introduce the microphone/voice input option early in course initiation; invite learners to try speaking a short request and compare it with typing. Present voice as an optional workflow, not a requirement.
- **Implementation notes:** Verify whether the microphone uses dictation or another voice interaction workflow in the tested IDE version. Explain how to review/edit transcribed text before submission and remind learners not to speak confidential or sensitive information into unapproved tools or settings.
- **Evidence:** User observation; no new screenshot attached. Prior Antigravity screenshots show a microphone icon near the chat composer.
- **Status:** suggested enhancement

### 2026-10-24 · Antigravity setup / early lessons · Disable unsolicited typing and code suggestions
- **ID:** NOTE-003
- **IDE:** Antigravity
- **Type:** instructional improvement | IDE configuration | learning environment
- **What works:** Antigravity offers inline code completion and related predictive typing features.
- **Opportunity:** These features can insert or suggest text that is not part of the course exercise, making beginners' results harder to reproduce or confusing who authored the content.
- **Expected:** Include an optional, explicit pre-course setup step to turn off automatic code/typing suggestions during guided exercises, while leaving tutor chat and deliberate agent edits enabled.
- **Implementation detail:** Antigravity documents individual toggles for **Autocomplete**, **Supercomplete**, **Tab-to-Jump**, and **Tab-to-Import**. Check all four in the tested version's Settings. Verify separately whether standard editor suggestions/quick suggestions remain enabled. Do not assume disabling one feature disables all suggestions. Restore settings at the end if desired.
- **Evidence:** User observation (no screenshot supplied). Official documentation: https://antigravity.google/docs/ide/tab
- **Status:** suggested enhancement
