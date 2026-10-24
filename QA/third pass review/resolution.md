# QA pass 3: resolution

- **Scope:** Slice 1 new lessons (1.2, 2.2, 3A.1, 3B.1) and Slice 2 (1.3, 1.4, 2.1, 2.3, 2.4)
- **Setup:** Antigravity IDE 2.5.5, Windows, Review-driven development, Gemini 3.8 Flash (default)
- **Result:** no errors. Notes were friction points and suggestions, addressed below.

| # | Note | Resolution |
|---|---|---|
| 1 | `/start-course` ran `git status --short` before the terminal lesson; a new learner wouldn't know git or that it's safe | `AGENTS.md` → **Running commands**: no commands before 2.4; from 2.4, explain each command (what it is, that it's safe, that a box will pop up) before running it. `start-course` reads files instead of running commands. 1.2's command note updated. |
| 2 | @ file picking worked | Marked ✅ in `SCREEN_GUIDE.md` |
| 3 | Rule files have an **Activation Mode** toggle (Manual / Always On / Model Decision / Glob), so typing the `trigger:` header is duplicative | 2.1 now uses the toggle and checks for a duplicate header. `SCREEN_GUIDE.md` updated. Open: does the toggle write the header to disk itself? |
| 4 | 2.1's test answered in chat, not a file, and didn't say what to do next | The test prompt now saves to `workspace/week-1-actions.md`. Before any side trip, the tutor says what to type when done (`/next-step`). `AGENTS.md` → **Side trips**: any conversation that finishes a non-course request during a lesson ends with "type `/next-step`". Same fix in 2.3. |
| 5 | Instructions + skills + memory reinforcement landed well | No change |
| 6 | The skill didn't run as expected; asking the agent produced a good diagnosis and fix | Made it a deliberate beat in 2.3 step 6: "compare what it did with what `SKILL.md` says." That's how you debug an agent. Added a sticking point. |
| 7 | Tab completes skill names | Added to `SETUP.md` step 8, the `/start-course` welcome, 2.3 step 6, and `SCREEN_GUIDE.md` |
| 8 | 2.4: prepare learners for the approval pop-up before the command runs | 2.4 step 4 now warns them first ("don't click yet, tell me what it does"). Verified: Review-driven development asks before every command. |
