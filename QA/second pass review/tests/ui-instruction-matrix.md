# UI instruction test matrix — Antigravity

These are proposed checks, not an implemented or executed test suite. Confirm against the specific Antigravity release used in the course.

| Test ID | Lesson | UI instruction or behavior | Evidence | Expected result | Status |
|---|---|---|---|---|---|
| UI-001 | All | Referenced IDE UI labels exist in tested version | Live UI needed | No unsupported controls or modes | Not run |
| UI-002 | All | Navigation instructions can be followed | Live UI needed | End state matches lesson goal | Not run |
| UI-003 | All | Screenshot-backed layout descriptions are accurate | Screenshots and live UI | No unverified fixed-position assumptions | Not run |
| UI-004 | All | File names and paths exist | Repository needed | Every referenced lesson artifact is accessible | Not run |
| UI-005 | All | Edit/review/accept workflow described accurately | Live UI needed | Instructions match actual IDE behavior | Not run |
| AG-UI-001 | Course initiation | Explain diff review and acceptance workflow | `../screenshots/note-001-change-approval.png` | Verify individual accept/reject and **Accept all**; avoid blind acceptance | Proposed; manual verification needed |
| AG-UI-002 | Progress tracking | Check recurring `progress.md` changes near chat composer | `../screenshots/note-001-progress-change-card.png` | Determine approval frequency and impact on saved progress | Proposed; manual verification needed |
| AG-UI-003 | Course initiation | Verify microphone input workflow and permissions | Earlier screenshots and live UI | Optional voice exercise works; typing fallback remains | Proposed; manual verification needed |
| AG-UI-004 | Pre-course setup | Disable unsolicited typing/code suggestions | Antigravity Tab docs and live UI | Guided writing has no unwanted completions; deliberate agent actions still work | Proposed; manual verification needed |
