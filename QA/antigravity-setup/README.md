# Antigravity IDE setup: reference screenshots

Captured by David on 2026-10-24 (Windows, fresh setup). The source for `SETUP.md` and `lessons/SCREEN_GUIDE.md`.

| # | Screen | Note |
|---|---|---|
| 00a–c | Download page (top / middle / bottom) | The **Antigravity App** comes first. **Antigravity IDE (Standalone)** v2.5.5 is near the bottom, under "Antigravity for IDEs." Annotated copies are in `docs/assets/setup/` |
| 01 | Welcome to Antigravity IDE: "Success, Continuing…" | Google sign-in happens *before* this. Not captured yet |
| 02 | Choose setup flow | Course says **Start fresh** |
| 03 | Select Theme | Any |
| 04 | How do you want to use the Antigravity IDE Agent? | Course says **Review-driven development** (Recommended). David chose Agent-driven for this run |
| 05 | Configure Your Editor | Normal + Recommended |
| 06 | Build with Google (plugins) | Leave unchecked |
| 07 | Security Notice & Data Use | Data-use box is **checked by default** |
| 08 | The IDE with the course open, `/start-course` running | Explorer / editor / agent panel; model shown: Gemini 3.8 Flash High |

## Second capture: fresh reinstall (2026-10-24, 07:17–07:25)

| # | Screen | Note |
|---|---|---|
| 10–15 | Windows installer: License → Destination → Start Menu → **Additional Tasks** → Ready → Finish | "Create a desktop icon" is **off by default**. SETUP tells learners to tick it |
| 20 | First launch: **Migrate Settings, Keybindings, and Extensions** dialog | Only because an older Antigravity install existed. Learners: **Cancel** |
| 21 | Agent panel: "To use the agent, please login **here**"; model "No Model Selected" | Plus the **Log in →** button, top right |
| 22 | Welcome to Antigravity IDE: **Continue with Google** | |
| 23–25 | Browser: Choose an account → "Make sure that you downloaded this app from Google" → **Sign in** → "You have successfully authenticated" + **Open Antigravity IDE?** | 23 and 24 show David's email. **Don't publish these** |
| 26 | Success, Continuing… → Next | Then the same first-run screens as 02–07 |
| 30 | `/start-course` typed: it becomes a **start-course** skill chip | ✅ Skills are invocable in the IDE. Default model: **Gemini 3.8 Flash High** |
| 31 | Start screen with no folder open: **Open Folder**, **Clone Repository**, Workspaces, Google Extensions | |
| 32 | Clone Repository: "Provide repository URL or pick a repository source" / **Clone from GitHub** | Needs Git installed. **Antigravity doesn't bundle Git** (checked the install folder) |

**Confirmed by David:** the trust prompt appears on first open; version **2.5.5**. **Still needed:** the review-an-edit UI (QA pass 2 lessons), the trust prompt, and what reviewing an AI edit looks like.
