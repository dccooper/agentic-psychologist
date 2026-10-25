# Site Plan: GitHub Pages (friends preview → v1)

*Draft, 2026-10-25. Replaces the site notes in PLAN §7.1 once agreed.*

## The phase we're in: a quiet public preview

- **The repo goes public** (decided 2026-10-25), but it isn't announced or marketed. Friends get a direct link.
- **GitHub Pages** hosts the site from `/docs` on `main`. Free on public repos, no build service needed.
- **The site asks search engines not to index it** during the preview (a `noindex` tag), so "public" stays "unlisted." Remove the tag at v1.
- Friends test the real thing: download, set up, run lessons, send feedback.

## Before the repo goes public (blockers)

| # | Item | Why | Recommendation |
|---|---|---|---|
| 1 | **QA screenshots** (38 in `QA/`) | Some show your email address and other personal details. They're also in **git history**, so deleting them now isn't enough. | Remove `QA/**/screenshots/` from the whole history (a history rewrite with `git filter-repo`, then a force push), and keep the QA notes (`.md`). Back up the screenshots locally first. Alternative: start the public repo with one fresh commit and keep the full history in a private backup. |
| 2 | **Commit email** | Every commit shows `4041893+dccooper@users.noreply.github.com`. | Use GitHub's private `…@users.noreply.github.com` address from now on. Optionally rewrite the existing commits to it in the same pass as #1. |
| 3 | **Module 4 lesson scripts** | The capstone ran from `planning/capstone-outline.md` (QA pass 5). Friends would hit "still being written" without scripts. | Write 4.1–4.5 from the outline. |
| 4 | **Repo name / URL** | The site URL is `dccooper.github.io/<repo-name>/`. `aug_psych` is a working name, and renaming after links go out breaks them. | Rename before sharing, e.g. `agentic-psychologist` → `dccooper.github.io/agentic-psychologist/`. |
| 5 | **Scrub check** | No test files ship (`QA/SHIP_SCRUB.md`). | ✅ Done 2026-10-25 (reset to zero). |

Not blockers, but check: the `observability/` folder is ignored and never pushed; `planning/` is fine to be public (it's how an educator can see the reasoning).

## Who the site is for

1. **Learners** (trainees, clinicians, researchers): "What is this, is it for me, how do I start?"
2. **Educators**: "Can I use this in my program, and how?"
3. **Friends testing now**: "What do I do, and how do I tell you what broke?"

## Pages

The **front page** is a showcase. Everything else sits in a **guide section** behind a menu. Theme: **Just the Docs** (clean, searchable, works on GitHub Pages as a remote theme), with a custom front-page layout.

| Page | Purpose | Source | Status |
|---|---|---|---|
| **Home** | What it is, who it's for, what you'll build, how learning inside the editor works, one big **Start in 5 minutes** button. "Free, open, no real patient data." | New | To write. Needs visual direction (your reference examples). |
| **Setup** | Download, install, sign in, get the course, start. | `SETUP.md` | Move to `docs/setup.md` as the single source; root `SETUP.md` becomes a pointer (Pages only builds `/docs`). Screenshots already in `docs/assets/setup/`. |
| **The course** | Modules, lessons, times, the two paths, what you make in each. Not the tutor scripts. | `lessons/README.md`, `OUTLINE.md` | To write (learner-facing, no answer keys). |
| **Real concerns about AI** | The top four concerns, then the FAQ (PLAN §8.5). | PLAN §8.5 | To write. The water comparison **needs sourced figures** (Assumption 11) or gets cut for the preview. |
| **For educators** | The lean guide (PLAN §8): where it fits, session maps, forking and adapting, before assigning, localization note. | PLAN §8, §8.1 | To write. |
| **Testing the preview** | For friends: what to test, how long it takes, how to log what goes wrong, where to send it. | `QA/` habits | To write. Remove at v1. |
| **About & credits** | Who made it, licenses (CC BY-SA content, MIT code), the dataset credit (Rung, OSF, CC BY 4.0), the reading-pack credit (PLOS ONE, CC BY 4.0), Antigravity disclaimer (not affiliated with Google). | `data/README.md`, licenses | To write. |
| **Learn more** | Curated outside resources (terminal, vibe coding, prompting). | Your Raindrop collections | Later (backlog). A placeholder link for now, or leave it out. |

**What the site does not show:** lesson scripts, answer keys, and the 3B.3b reveal notes. They're readable in the public repo (2.2 even says so), but the site doesn't advertise them.

## The download link

Use a direct ZIP link on the site: `https://github.com/dccooper/<repo>/archive/refs/heads/main.zip`. One click, no "Code → Download ZIP" menu. Update `SETUP.md` step 5 and the README to match. (The unzipped folder is named `<repo>-main`; SETUP should say so.)

## Feedback from friends

Friends may not have GitHub accounts. Options:

- **A short form** (Google Forms or similar): lesson, what happened, what you expected, a screenshot. Easiest for non-technical testers.
- **GitHub Issues** with a template, for testers who have accounts.
- **Email.** Simplest, hardest to track.

Recommendation: a form for everyone, with Issues as an option. Either way, ask testers **not to include screenshots that show their email or other personal information**.

## Build steps (once blockers are cleared)

1. `docs/_config.yml` (Just the Docs remote theme, site title, `baseurl` = repo name, `noindex` during the preview, exclude the screenshot source scripts).
2. Move `SETUP.md` → `docs/setup.md`; root pointer file.
3. Write the pages above (home last, once there's a visual direction).
4. Turn on Pages: Settings → Pages → Deploy from branch → `main` / `/docs`.
5. Check: the site loads, every link works, the ZIP link downloads, and setup works on a clean machine (PLAN §7.1).

## Open questions

1. **History:** rewrite to remove the screenshots (keeps history), or start fresh (simplest)? *Recommended: rewrite.*
2. **Repo name** for the URL? *Recommended: `agentic-psychologist`.*
3. **Visual direction** for the home page: your reference examples (PLAN §7.1 has been waiting on these).
4. **Feedback channel:** form, Issues, or email? *Recommended: a form, with Issues as an option.*
5. **Course title:** is "The Agentic Psychologist" final enough to put on a site? (It's still marked "working title.")
6. **Concerns page in the preview:** ship it with the water comparison cut until it's sourced, or hold the whole page? *Recommended: ship it, cut the comparison.*
