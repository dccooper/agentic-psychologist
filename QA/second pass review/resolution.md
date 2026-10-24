# Resolution: QA Pass 2 (Antigravity IDE 2.5.5, lessons 0.1 to 1.1)

Fixed 2026-10-24. **Result of the pass: no bugs.** Lessons 0.1, 0.2, and 1.1 completed. The tutor saved progress, checked answers, and followed the scripts. The three notes are improvements. **Changes need a retest.**

| Item | Decision and fix | Files |
|---|---|---|
| **NOTE-001** Review and approval friction | **Graduated approach.** (1) 0.1: the first edit (the learner's name) introduces the **Files With Changes** bar, with "glance, then Accept all" and no deep dive. (2) 1.1: real review using the verified controls (the **Review** card, per-block **Accept/Reject**, the **Accept Changes** bar, and what **Accept all** means). (3) After 1.1: **Accept all** is fine for routine `progress.md` updates after a glance; the learner's own work always gets a real look. (4) 1.2: approval fatigue taught on purpose, and **Accept all ≠ automatic approval**. The course never turns on auto-approval. **Less noise:** the tutor now saves `progress.md` only at pause points, lesson ends, and when stopping, not after every checkpoint, and no longer re-saves just because `/start-course` ran. | `AGENTS.md`, `start-course` + `next-step` skills, `0.1`, `1.1`, `OUTLINE.md` (1.2), `SCREEN_GUIDE.md` |
| **NOTE-002** Voice input | An optional one-liner in 0.1 step 4: the **microphone** lets you speak instead of type; read before sending; nothing confidential by voice either. Not a required step. Behavior and permissions are marked ⚠️ in the screen guide. | `0.1-welcome.md`, `SCREEN_GUIDE.md` |
| **NOTE-003** Unsolicited typing suggestions | New **SETUP step 7 (recommended, skippable)**: turn off Autocomplete, Supercomplete, Tab-to-Jump, and Tab-to-Import, explained as keeping clear *what you wrote vs. what the AI wrote*. The settings location comes from Google's docs page, which names the toggles but not the menu path, so it's marked ⚠️. | `SETUP.md`, `SCREEN_GUIDE.md` |

**Hypothesis to verify (from the screenshots):** pending edits are already written to the file. Reject reverts them, and Accept keeps them. If true, progress saves even before acceptance.

**Next retest:** 0.1 (the first-edit explainer), 1.1 step 6 (review walkthrough), SETUP step 7 (find the Tab settings and screenshot them), and a check that `progress.md` changes now appear only at pause points and lesson ends.
