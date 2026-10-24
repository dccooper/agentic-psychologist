# UI instruction test matrix (initial)

| Test | Course step | Claim/action to verify | Screenshot evidence | Current result |
|---|---|---|---|---|
| UI-001 | Course initiation / Step 2 | Instructions tell learner where to find Files / Browse Files and `world/artifacts/welcome-email.md` | `../screenshots/issue-001-before.png`, `../screenshots/issue-001-after.png` | FIXED, needs retest (QA-001) |
| UI-002 | Lesson 0.1 / completion | Instructions identify actual editing-capable chat mode and provide successful `workspace/progress.md` save path | `../screenshots/issue-003-mode-picker.png` | FIXED, needs retest (QA-003) |
| UI-003 | Lesson 1.1 / regions | Identify chat, editor and file explorer correctly on captured Cursor UI | `../screenshots/issue-004-cursor-layout.png` | FIXED, needs retest (QA-004) |
| UI-004 | Every UI-dependent lesson | All menu/button labels match the reference UI state | Capture missing reference screenshots | NOT RUN |
| UI-005 | Every UI-dependent lesson | All specified files exist at expected paths | Needs repository/course files | NOT RUN |
| UI-006 | Every UI-dependent lesson | Hidden/rearranged panels have recovery instructions | Needs alternative-layout capture | NOT RUN |

| UI-007 | Lesson 1.1 / reviewing edits | Two-files-changed card, Review entry point, and actual accept/reject controls match lesson wording; distinguish `first-week.md` and `progress.md` | `../screenshots/issue-005-review-changes.png` (pre-review only) | FIXED, needs retest (QA-005); post-review controls need verification |

Current screenshots capture isolated states and cannot substitute for an automated Cursor UI session. Follow up by identifying the exact build/version and enumerating remaining lesson scripts.
