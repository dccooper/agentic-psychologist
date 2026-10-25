# Home page design guidelines

The Agentic Psychologist · University of Tomorrow, Department of Experimental Theoretical Psychology

This folder starts with an underscore, so Jekyll does not publish it. The logo files and token CSS live in `assets/`, which Jekyll does publish.

## 1. What the page is for

The page has one job: give psychologists who don't know where to start with AI a place to start. Every decision on it was tested against two questions.

1. Would a nervous clinician click Start?
2. Would a skeptic keep reading?

When a future change is debated, use the same two questions. "Which looks cooler?" is not one of them.

## 2. Decisions made, round by round

| Round | Variable | Winner |
|---|---|---|
| 1 | Direction | Calm, practical page (C) with the University of Tomorrow confined to one section (from B) |
| a | Headline | Leads with ease: 20-minute lessons, no coding |
| a2 | Problem statement | Eyebrow line above the headline |
| b | How much of the world shows | The orientation packet only. No letterhead strip, no compliance joke in safety |
| c | Hero visual | Department memo |
| d | Button wording | "Start in 5 minutes" |
| e | Section order | Packet before safety, so safety and the FAQ form one serious block |
| f | Color and type | Harbor: white, slate, harbor blue, Atkinson Hyperlegible |
| Logo | Mark | The Sun That Hasn't Quite Risen (shield) |

## 3. The humor rule

Humor goes where people learn what the course is: the hero memo and the orientation packet. It stays out of safety, privacy, cost, the FAQ answers and the button. A skeptic should never have to read past a joke to reach an answer.

Tone, when humor appears: dry, warm and institutional, in the spirit of Terry Pratchett and vaudeville. The joke is always on the institution (the coffee machine, the registrar, the paperwork). Never on clients, mental illness, or the reader.

## 4. Page structure and copy

Sections in order. Copy marked [brackets] still needs filling.

### 4.1 Top bar

- Left: "The Agentic Psychologist" (bold, 17px).
- Right: The course · Real concerns · GitHub.
- No university branding here. It appears first in the memo.

### 4.2 Hero

Two columns on desktop, stacked on phone (text first, memo second).

- Eyebrow (accent color, bold): For psychologists who don't know where to start with AI
- Headline (h1): Learn the basics of AI agents in 20-minute lessons. No coding required.
- Subhead: A free course for trainees, clinicians and researchers. A tutor inside the tool walks you through it one step at a time, so you leave with a foundation to build on.
- Primary button: Start in 5 minutes (links to the setup guide)
- Secondary link: Real concerns, answered
- Trust line (muted, 14px): Free · Open source · No real patient data, ever

### 4.3 The memo (hero visual)

A sheet of paper rotated -1°, with a second sheet peeking out behind it at +2°. Paper color stays light in dark mode.

```
University of Tomorrow
Department of Experimental Theoretical Psychology        MEMORANDUM
-------------------------------------------------------------------
TO:    New students (you)
FROM:  Office of New Students, Room 0.5
RE:    Your first day, which is today
DATE:  Tomorrow, as usual

Welcome. Your tutor is already inside the editor and has been
rehearsing. Type /start-course and it will take things one step
at a time.

Lessons last about twenty minutes, which is roughly how long the
kettle takes now that the coffee machine is temporarily out of order.

Please bring curiosity. Questions of any size are welcome, including
the ones you think are silly.

M. Pending                                    [ ADMITTED ]
Acting Deputy Assistant Registrar             (provisionally)
```

- Letterhead uses the small crest mark at about 34px.
- The memo is real text, not an image. Screen readers read it as a normal article.
- The stamp is decorative: rotated -8°, accent color, mono.

### 4.4 How it works

A surface-colored band with three cards.

1. Step 1 · [time] · Download Antigravity
2. Step 2 · [time] · Open the course folder
3. Step 3 · [time] · Type `/start-course`

Fill in real timings. They should add up to roughly the "5 minutes" on the button.

### 4.5 Orientation packet (the only in-world section)

A bordered box with a dark letterhead strip on top: crest mark, "University of Tomorrow", "Department of Experimental Theoretical Psychology", and the motto in italics, "Tomorrow's Treatments, Today's Stress".

Inside, on the surface color:

- Heading: Welcome to the Department. Here's what you'll do.
- Intro: Everyone starts with the same orientation. Then you pick a rotation, and you graduate with an agent that's yours to keep.
- PSY 101 · Core curriculum: An agent = instructions + skills + memory. Every lesson adds to one of the three.
- Clinic rotation: Build a chief of staff for a busy clinic director. Then make the clinic a website. Aside: The director's door sign reads "Knock. Then knock again."
- Lab rotation: Build a literature-review agent. Then run a real analysis on open data and check it against the published, peer-reviewed version. Aside: [lab joke]
- Graduation · Capstone: Move your agent out of the course and make it your own.
- Three small asides:
  - Timetable: Lessons run about 20 minutes. Stop and resume any time.
  - Your tutor: Lives inside the editor. Never tires of the same question.
  - Facilities: The coffee machine is temporarily out of order. It has been for years.
- Link below the box: See the full course outline

### 4.6 Safety and cost (no jokes)

Two-column checklist with green checkmarks.

- Never real patient or participant data. Practice data is provided.
- Free plan. Antigravity's free tier has weekly usage limits; lessons pause and resume.
- Open. Content CC BY-SA, code MIT.
- No tracking on this site.

Keep "free" honest. If Antigravity's plan terms change, update this line first.

### 4.7 Questions skeptics ask (no jokes in answers)

Use native `<details>`/`<summary>` so it works without JavaScript and with a keyboard.

- Is it really free?
- I've never used a code editor. Can I do this?
- What happens to what I type?
- Should psychologists be doing this at all?
- Is the University of Tomorrow real? (The answer can smile. It is the one FAQ about the world, not about risk.)
- Link: All real concerns

### 4.8 Footer

The Agentic Psychologist · CC BY-SA 4.0 · MIT · GitHub

## 5. Color (Harbor)

Defined as CSS custom properties in `assets/css/uot-tokens.css`. Light is the default, and dark follows `prefers-color-scheme`.

| Token | Light | Contrast | Dark | Contrast | Use |
|---|---|---|---|---|---|
| `--uot-page` | #FFFFFF | | #121A1E | | Page background |
| `--uot-surface` | #EEF3F5 | | #1B262C | | Bands, packet body |
| `--uot-text` | #1E2A30 | 14.7:1 | #E6EDF0 | 14.9:1 | Body and headings |
| `--uot-muted` | #4F5D64 | 6.8:1 | #A9B7BE | 8.6:1 | Secondary text |
| `--uot-accent` | #1F5F7A | 7.1:1 | #7FC0DA | 8.8:1 | Links, button fill, eyebrow |
| `--uot-on-accent` | #FFFFFF | 7.1:1 | #0E1A20 | 8.8:1 | Button text |
| `--uot-check` | #2E6B4F | 6.3:1 | #7CC79F | 8.8:1 | Safety checkmarks |
| `--uot-border` | #D5DDE1 | decor | #2E3C43 | decor | Rules and card borders |
| `--uot-paper` | #FFFEFA | | #EDE9DF | 12.1:1 text | Memo sheet |
| `--uot-strip` | #1E2A30 | | #E6EDF0 | | Packet letterhead strip |

Contrast is against that mode's page background (buttons against their own fill). Don't add a second accent. If a new color is needed, check it against these backgrounds at 4.5:1 for text.

## 6. Type

- One family: Atkinson Hyperlegible, regular and bold, self-hosted from `assets/fonts/` (SIL Open Font License). No Google Fonts call at runtime.
- Mono: system stack, for `/start-course`, memo headers and notice labels.

| Role | Size / line height | Weight |
|---|---|---|
| h1 (hero) | 48px / 1.1 desktop, 30–32px phone | 700 |
| h2 (sections) | 28–30px / 1.2 | 700 |
| Card title | 18–20px / 1.3 | 700 |
| Body | 18–19px / 1.55 | 400 |
| Small and muted | 14–15px / 1.45 | 400 |
| Mono labels | 12–13px, uppercase, letter-spacing .06em | 700 |

Use `clamp()` for the h1 so it scales between phone and desktop, for example `font-size: clamp(2rem, 4vw + 1rem, 3rem)`.

## 7. Components

- Primary button: accent fill, on-accent text, 14px × 24px padding, 6px radius, at least 44px tall. Only one on screen at a time.
- Links: accent color, underlined in body text. Nav links can drop the underline but must show it on hover and focus.
- Step card: page-colored card on the surface band, 1px border, 8px radius.
- Notice (packet): page-colored card, 1px border, 4px accent top border, 4px radius, mono uppercase label.
- Aside (packet): dashed border, smaller text. Used only for the jokey asides.
- Checklist item: 22px check icon (stroke, `aria-hidden="true"`), bold lead phrase, plain explanation.
- Memo: see 4.3. Never use the memo style for anything about safety or cost.
- Focus: a 3px outline in the accent color with a 2px offset, on every interactive element.

## 8. Logo

Files in `assets/logo/`:

| File | Use |
|---|---|
| `uot-crest.svg` / `uot-crest-dark.svg` | Full crest with motto ribbon. 120px wide or larger |
| `uot-mark.svg` / `uot-mark-dark.svg` | Simplified shield (sun, three rays, psi). 24–120px |
| `uot-lockup.svg` / `uot-lockup-dark.svg` | Mark plus "University of Tomorrow" and the department name |
| `favicon.svg` | 32px mark. Switches colors with the browser's color scheme |

The idea: tomorrow's sun is just cresting the horizon and, being tomorrow's, never gets any further. Psi stands for the department. The crest says it was founded tomorrow.

Rules:

- Two colors only: ink (`--uot-text`) and accent (`--uot-accent`). Use the `-dark` files on dark backgrounds.
- Leave clear space at least the width of the psi on every side.
- Use the full crest only where it can be 120px wide or more. Below that, use the mark.
- Don't recolor the rays to anything but the accent. Don't add gradients or shadows, and don't put it on a busy background.
- The SVG text uses Atkinson Hyperlegible with Arial as a fallback, and Georgia for the psi. Before print or merchandise, convert the text to outlines in a vector editor.

## 9. Accessibility

- Text contrast is at least 4.5:1 everywhere (see section 5).
- Every tap target is at least 44px.
- Use real `<a>`, `<button>`, `<details>` and `<h1>`–`<h3>` in order. Never a clickable `<div>`.
- Decorative SVGs get `aria-hidden="true"`. The crest in the packet strip gets `alt="University of Tomorrow crest"`.
- Rotated elements (memo, stamp) are text. Don't rotate anything more than 2° except the stamp.
- Respect `prefers-reduced-motion`. The page has no motion now, so keep it that way.
- Test at 390px wide: everything stacks, nothing scrolls sideways, and the memo follows the hero text.

## 10. Fitting into Just the Docs

Check these against the Just the Docs version in your `Gemfile.lock`.

- Layout: give the home page a full-width layout without the sidebar. Recent Just the Docs versions ship `layout: minimal`. If yours doesn't, add `_layouts/home.html` that extends `default` and hides the nav.
- Styles: put home-only styles in `_sass/custom/custom.scss`, scoped under a wrapper class such as `.uot-home`, so the course pages are unaffected. Load `assets/css/uot-tokens.css` from `_includes/head_custom.html`.
- Course-page colors: create `_sass/color_schemes/harbor.scss` with `$link-color: #1F5F7A;`, `$btn-primary-color: #1F5F7A;` and `$body-text-color: #1E2A30;`, then set `color_scheme: harbor` in `_config.yml`. Just the Docs compiles color schemes at build time, so automatic dark mode on the course pages needs either its built-in `jtd.setTheme()` switch or a small `prefers-color-scheme` override in `custom.scss`. The home page handles dark mode on its own through the tokens.
- Favicon: in `_includes/head_custom.html`, add `<link rel="icon" href="{{ '/assets/logo/favicon.svg' | relative_url }}" type="image/svg+xml">`.
- Hide from search engines while you share it with friends: add `<meta name="robots" content="noindex, nofollow">` to `head_custom.html` (site-wide) or to the home page's front matter through a conditional. A `robots.txt` with `Disallow: /` helps too, but the meta tag is what reliably keeps pages out of results. Remove both at launch.
- No tracking: leave `ga_tracking` unset in `_config.yml`, and don't add analytics includes.

## 11. Still to fill

- [ ] Step timings in How it works
- [ ] Lab rotation joke
- [ ] The tutor's real first message, if you want it quoted anywhere
- [ ] Answers for the five FAQ items
- [ ] Download Atkinson Hyperlegible into `assets/fonts/`
- [ ] Remove noindex at launch
