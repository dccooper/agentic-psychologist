# Ship scrub: test-run files to remove before release

The course is tested by running it in this same folder, so test runs leave **learner files** behind. If any of these get committed, every learner would download someone else's finished exercises. Scrub before every release (v1, and any ZIP sent to testers).

## The rule: what ships in the learner folders

Only these files ship in the two folders learners write to:

| Folder | Ships | Everything else there is test-run output |
|---|---|---|
| `workspace/` | `progress.md`, **in its blank starting state** (as committed) | ✅ remove |
| `.agents/` | `skills/start-course/`, `skills/next-step/`, `skills/im-stuck/`, `skills/my-progress/` (plus any course skill added later; list it here). **Never ship skills learners build** (`meeting-to-actions`, `tidy-up`, `weekly-plan`, `lit-matrix`, …). | ✅ remove (e.g. `.agents/rules/`, `skills/meeting-to-actions/`) |

Learner work outside these folders shouldn't exist. If `git status` shows a new file anywhere else after a test run, check it before committing.

## Check and scrub

```
git status --short --untracked-files=all workspace .agents
```

- **Untracked (`??`)** files there are test output. Delete them (`git clean -n workspace .agents` to preview, then `-f` to delete).
- **Modified (`M`) `workspace/progress.md`** → restore the blank version: `git checkout -- workspace/progress.md`.
- **Never** `git add workspace` or `git add .agents` wholesale. Add course files by path.

## Known test-run files (as of QA pass 3, 2026-10-24)

From David's runs through Slices 1–2. Kept on disk on purpose (his live progress) and **not** committed.

- `workspace/progress.md` (modified: Dave, Lab path, all of Slices 1–2 complete)
- `workspace/my-rule.md` (0.2)
- `workspace/my-notes/first-week.md` (1.1)
- `workspace/drive-plan.md`, `workspace/shared-drive-practice/**` (1.2, 11 files)
- `workspace/meeting-actions.md`, `workspace/drafts/reply-to-okafor.md` (1.4)
- `workspace/templates/action-items.md`, `.agents/rules/my-style.md` (2.1)
- `.agents/skills/meeting-to-actions/SKILL.md`, `workspace/actions/*.md` (2.3, 2 files)
- `workspace/clinic/project-brief.md` (3A.1), `workspace/lab/project-brief.md` (3B.1)

Path lessons (3A.2 onward, 3B.2 onward) will add more under `workspace/clinic/`, `workspace/lab/`, `workspace/actions/` and new `.agents/skills/*`. The rule above catches them. Add notable ones here after each QA pass.

**Expected from Slice 3 (paths):**
- Both paths: `.agents/skills/tidy-up/`, `workspace/INDEX.md`, `workspace/archive/**`.
- Clinic: `workspace/clinic/chief-of-staff/**` (instructions, memory, plans, prep), `workspace/clinic/website/index.html`; skills `weekly-plan`, `meeting-prep`, `wrap-up` (and stretch `whats-slipping`, `referral-one-pager`).
- Lab: `workspace/lab/lab-agent/**`, `workspace/lab/analysis/**`; skills `lit-matrix`, `weekly-lab-update`, `lab-wrap-up` (and stretch `paper-summary`).
- ⚠️ **`workspace/lab/reveal/` contains the authors' paper and R scripts, downloaded in 3B.3b. Never commit it.** (It's in `.gitignore` as a guard.) Committing it would break the blind comparison for every future learner (the firewall in `lessons/OUTLINE.md`).

## Also before release

- `QA/` screenshots that show personal info (email, names, other repos): scrub or remove (PLAN §7.1 launch checklist). Decide whether `QA/` ships at all.
- `progress.md` **Notes** written during testing (UI observations) belong in `SCREEN_GUIDE.md` or a QA log, not the shipped file. Restoring it covers this.
