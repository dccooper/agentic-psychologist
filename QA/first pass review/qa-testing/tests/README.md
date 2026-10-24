# Cursor UI instruction regression checks — proposed testing suite

Purpose: prevent course navigation instructions from drifting from the actual supported Cursor interface.

## Principle
A screenshot is evidence of a *specific UI state*, not proof of every possible configuration. Cursor versions, operating systems, selected chat modes, panels, and user preferences may vary. Do not promise that visual matching alone can certify instructions.

## Suggested process
1. Inventory UI-facing sentences in each lesson (location words, named buttons/menus, mode names, click sequences, expected file paths, and actions such as editing/saving).
2. Record the supported Cursor version/build, OS, viewport, theme and visible/hidden panel state for each screenshot fixture. These are **unknown** for the current provided screenshots except the OS appears to be Windows; confirm before treating them as a release baseline.
3. Capture reference screenshots for each action at the relevant lesson step: initial state, optional menu opened, and successful destination.
4. Static checks: flag brittle language (`left`, `right`, `middle`, `Agent mode`, etc.) for review; verify file names and paths against checked-in lesson assets; validate checkpoint targets.
5. Visual review: compare instructions to the captured screen and record **pass**, **fail**, or **needs review** with evidence. A vision-based checker may propose findings, but uncertain labels or alternate layouts require human verification.
6. End-to-end learner run: follow the instructions literally in Cursor. Test both default UI and relevant alternate pane configurations.
7. Run after updating any lesson navigation, supported Cursor build, or screenshots. Reclassify stale screenshot fixtures, don't silently edit evidence.

## Proposed test record fields
`id | lesson | Cursor version | OS | UI state | instruction | screenshot | expected action | outcome | reviewer | date`

## Known regression cases
- QA-001: Lesson 0.1 welcome email — do not assume Files explorer is on left; include Files > Browse Files (when needed).
- QA-003: Ask mode to editing-capable chat mode — visible mode choices and how to actually save progress.
- QA-004: Lesson 1.1 panel identification — match the pictured chat/editor/file explorer and provide adaptive instructions.

See `ui-instruction-matrix.md` for the initial set of test cases. This is a test **specification**, not an implemented UI automation harness.
