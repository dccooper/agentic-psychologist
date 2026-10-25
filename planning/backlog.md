# Backlog: ideas and cleanups for later

Things the author has flagged for later, so they don't get lost. Newest first. Move an item into a lesson or `PLAN.md` when it's picked up.

## Before v1 (do once the lesson list is final)

- **Renumber lessons without a/b suffixes** (QA pass 4). For example, 3A.2a and 3A.2b become 3A.2 (or 3A.2 and 3A.3), not split by letter. Touches lesson file names, `lessons/README.md`, `OUTLINE.md`, cross-references inside lessons, `progress.md`'s template, and the site. Do it in one pass at the end, then retest `/start-course` and `/next-step`.
- **Scrub test-run files** (`QA/SHIP_SCRUB.md`).

## Open questions to discuss

- **The terminal lesson (2.4).** It introduces the terminal but doesn't connect back to later lessons. Options: keep and connect it, shrink it to a mention, or hold it for v2. *Waiting on a discussion with the author; don't change it yet.* (QA pass 4)
- **`world/artifacts/` is getting cluttered** (about 20 files by the end of the paths). Options: (a) organize it into folders by where it's used (`department/`, `clinic/`, `lab/`); (b) leave it, and make tidying up part of a lesson. (QA pass 4)

## Candidate additions (later, maybe v2)

- **Agents as tech support.** From a talk the author attended: psychologists can use agents and LLMs for everyday tech support (an error message, a settings problem, a spreadsheet formula, "why won't this print"). Builds on 2.4 and 3B.3a's install-with-the-agent moment. Possible home: a capstone side lesson or an idea-gallery entry (see `planning/capstone-outline.md`). (QA pass 4)
- **Writing papers in LaTeX with an agent.** Draft in Markdown, have an agent build and iterate on a LaTeX version (layout, references, figures). Common outside the social sciences. Needs a LaTeX install (or Overleaf, no install). Possible home: a Lab-path or capstone side lesson. (QA pass 4)
- **The screenshot exercise** dropped from 1.4 (asking the AI about a pasted image, e.g. the Annex whiteboard). (Slice 2)
- **A Git bonus in Graduation:** install Git, re-clone, get course updates with a pull. (PLAN §7.1)
