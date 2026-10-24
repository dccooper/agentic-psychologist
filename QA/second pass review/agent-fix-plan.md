# Agent Fix Plan — Vertical Slice 2 (Antigravity)

## Context
This is a new Antigravity IDE test run. Do not assume Cursor's UI or previous issues are present. Use captured evidence to reproduce failures.

## Prioritized fixes

### NOTE-001 — Progressive review-and-approval instruction
**Priority:** Design consideration for early course and subsequent modules (not a defect).

**Recommendation:**
1. In course initiation, explicitly explain the diff (added/removed text), **Accept**, **Reject**, **Review**, and **Accept all** as those controls appear in Antigravity; do not require exact labels in other IDEs without validating them.
2. Have the learner intentionally inspect and approve/reject initial edits, including changes to `workspace/progress.md`.
3. Later teach a graduated approach: for small, routine, understood edits, the learner may review a batch and use **Accept all**; for substantive edits, inspect files or individual hunks first.
4. Do not silently enable automatic approvals or equate batch **Accept all** with auto-accepting future tool actions. If exploring automatic approvals later, make it an explicit optional lesson with clear boundaries and rollback guidance.
5. Test whether every edit to `workspace/progress.md` appears in a **1 File With Changes** card above the chat composer, and whether the learner must approve it to persist progress. This is a hypothesis based on two screenshots, not yet confirmed as universal behavior.
6. Consider batching routine progress updates or intentionally prompting approval at meaningful checkpoints to avoid repeated interruption. Do not assume that automatic acceptance is safe or available.
7. Teach the distinction between the **chat change card** (file-level controls) and the **editor diff** (specific changes) using actual screenshots.
8. Keep the course's core principle: the learner remains responsible for checking AI-produced changes.

**Acceptance criteria:**
- Early lessons describe how to inspect an actual proposed edit and make a deliberate approval choice.
- Later lessons reduce repeated approval friction without telling beginners to blindly accept all changes.
- Instructions match the Antigravity controls shown in the screenshot or explain layout/version variability.
- Any discussion of automatic approval distinguishes it from a one-time **Accept all** action.

**Evidence:** `screenshots/note-001-change-approval.png`, `screenshots/note-001-progress-change-card.png`


For each finding, capture root-cause hypothesis (clearly labeled), proposed fix, files likely affected (when known), and acceptance criteria. Group overlapping fixes when supported by evidence.

## Validation requirements
- Confirm all referenced lesson paths exist.
- Check instructions against the tested Antigravity interface and configuration.
- Validate the actual navigation and interaction sequence, not just visual labels.
- Review source content for fidelity, and preserve the intended learning outcome.
- Note any steps requiring manual verification.

### NOTE-002 — Introduce optional voice input early
**Priority:** Low–medium, onboarding improvement (not a defect).

**Recommendation:** Early in course initiation, point out the microphone control in the Antigravity chat composer and offer a short, optional practice prompt using speech input. Explain that learners can inspect and correct generated text before sending, where supported. Verify exact control behavior and any permission flow for the tested version before writing fixed UI instructions. Keep text input equally supported and do not imply voice is universally preferred by developers. Add a privacy reminder for clinical/confidential material.

**Acceptance criteria:** Learners see an optional voice-input introduction; the instructions match the available Antigravity UI; voice is not required to progress; the tutor reinforces proofreading and approved-data boundaries.

### NOTE-003 — Prevent unsolicited code and typing suggestions during the tutorial
**Priority:** Medium, onboarding and reproducibility improvement (not a confirmed defect).

**Recommendation:** Add a short, reversible Antigravity preflight configuration step. In Antigravity Settings, verify and disable **Autocomplete**, **Supercomplete**, **Tab-to-Jump**, and **Tab-to-Import** during guided exercises as appropriate. Confirm whether regular editor quick suggestions also need disabling, and document the correct controls for the tested version. Do not disable the chat agent or its explicitly requested edits. Explain that the objective is to separate what the learner types from predictive IDE edits. Offer restoration instructions after the course.

**Acceptance criteria:** A novice can follow the instructions; typing into course files does not trigger unwanted AI completions or predictive Tab edits; deliberate tutor interactions and proposed file changes still work; settings are reversible and version-checked.

**Evidence:** Learner report; feature toggles are documented at https://antigravity.google/docs/ide/tab (actual settings location to be verified in the tested UI).
