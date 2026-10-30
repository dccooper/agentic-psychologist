---
title: Setup
nav_order: 2
description: Install Antigravity IDE, sign in, open the course, and start. About 15 minutes.
---

# Setup: getting ready
{: .no_toc }

<details open markdown="block">
  <summary>On this page</summary>
  {: .text-delta }
- TOC
{:toc}
</details>

You'll install a free app called **Antigravity IDE** (what's an IDE? see below), sign in with a Google account, and open the course in it. After that, the course teaches itself: an AI tutor inside the app takes over.

**There are 8 steps.** Take them one at a time. Each step ends with a **✅ Done when** line, so you know it worked before you move on.

> **You don't need any technical experience.** If something here doesn't match your screen, that's normal (apps update often). Take your best guess, and once the tutor is running, tell it what happened.

## Watch first: the orientation video (6 minutes)

{% include youtube.html id="KRvJdiSAlo8" title="New Student Orientation: Installing Antigravity IDE for The Agentic Psychologist" %}

The video walks through every step on this page, with captions. Prefer reading? The written steps below cover the same ground, and they're handy to keep open while you install. *(Curious how the video was made? See [How the video was made]({{ '/video/' | relative_url }}).)*

## First: what's an "IDE"?

**IDE** stands for **integrated development environment**. That's a technical name for a simple idea: **one app that keeps everything for a project in one window.** You get a list of your files, a place to read and edit them, and (in newer IDEs) an **AI assistant that can work on those files with you**.

Programmers use IDEs to write software, but you don't need to be a programmer to use one. Picture a word processor and a filing cabinet in the same window, with a capable assistant beside you who can read your documents and make changes you approve.

**Fair warning: it's going to look technical.** Antigravity is built for programmers, so the first time you open it you'll see a lot of panels, icons, and file names that look like code. **That's normal, and you won't need most of it.** You'll use three parts:

- **The agent panel:** where you talk to the tutor. You'll spend most of your time here.
- **The Explorer:** the list of files, like a filing cabinet.
- **The editor:** where a file opens when you click it, like a word processor.

You can ignore everything else (the icons along the edge, the bar at the bottom, most of the menus). The tutor will point out anything else when you need it.

**Why put up with an unfamiliar app instead of using a chat website like Gemini or ChatGPT?** Because this is where AI stops just *talking* and starts *doing work*. On a chat website, the AI only sees what you paste in, and its answers disappear when you close the tab. Here, it can open your files, draft new ones, and make changes **that you review and approve first**. It can also keep notes in files, so your work is still there tomorrow. That's what an **agent** is, and learning to direct and check one is the point of this course. (It's also how the course teaches itself: the tutor is an agent that reads the lesson files and saves your progress.)

**Think of your first day with an electronic health record.** It looked overwhelming then too, and within a week you only noticed the five things you actually use.

**Antigravity IDE** is Google's free IDE with a built-in AI agent. Google makes several products called "Antigravity," which is why step 1 is careful about which one to download.

*(Curious for more? Wikipedia has a short overview: [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment). You don't need it for the course.)*

---

## Step 1 of 8: Download the right app

1. Go to **[antigravity.google/download](https://antigravity.google/download)**.
2. Near the top, make sure your kind of computer is selected (**macOS**, **Windows**, …). It's usually picked for you.
3. ⚠️ **The first download on the page is the wrong one.** It's called **Antigravity App**, and it's a different product. **Don't click its buttons. Scroll down.**

   ![The top of the download page: the computer type is already selected; the first section, "Antigravity App," is the wrong download]({{ '/assets/setup/download-1-not-the-app.png' | relative_url }})

4. Keep scrolling past **Antigravity CLI** (commands in boxes) and **Antigravity for IDEs** (Visual Studio Code, JetBrains, Zed, Xcode, each with a **View Docs** button). You don't need any of these.
5. Near the bottom, find **Antigravity IDE (Standalone)**. Its heading is smaller than the others, so it's easy to miss. **This is the one you want.**

   ![Near the bottom of the page: "Antigravity IDE (Standalone)" with its Download buttons]({{ '/assets/setup/download-2-ide-standalone.png' | relative_url }})

6. Click the button for your computer:
   - **Windows:** **Download for x64** works for almost all Windows PCs. Choose **ARM64** only if your laptop has a Snapdragon / ARM chip. To check, go to **Settings → System → About → System type**.
   - **Mac:** **Download for Apple Silicon** if your Mac has an M1, M2, M3 or newer chip. Choose **Download for Intel** for older Macs. To check, open **Apple menu → About This Mac → Chip / Processor**.

**✅ Done when:** the installer file is in your **Downloads** folder.

---

## Step 2 of 8: Install it

Open the file you downloaded (usually in your **Downloads** folder).

**Windows**, the installer's screens:

| Screen | What to do |
|---|---|
| **License Agreement** | Choose **I accept the agreement** → **Next** |
| **Select Destination Location** | Leave it as is → **Next** |
| **Select Start Menu Folder** | Leave it as is → **Next** |
| **Select Additional Tasks** | ✅ **Tick "Create a desktop icon"** (it's off by default, and it makes the app easy to find). Leave the other boxes as they are → **Next** |
| **Ready to Install** | **Install** |
| **Completing the Antigravity IDE Setup Wizard** | Leave **Launch Antigravity IDE** ticked → **Finish** |

**Mac:** open the `.dmg` file and drag **Antigravity IDE** into **Applications**. Then open it from Applications.

**✅ Done when:** Antigravity IDE is open on your screen.

---

## Step 3 of 8: Sign in with Google

The app opens to an empty window. On the right, the agent panel shows a warning: *"To use the agent, please login here."*

1. Click **here** (or the blue **Log in →** button at the top right of the window).
2. On **Welcome to Antigravity IDE**, click **Continue with Google**. Your web browser opens.
3. **Choose an account** (or **Use another account**). **A personal Google account is simplest.** University Google accounts sometimes block new apps. (The course never uses real patient or research data, so a personal account is fine.)
4. Google shows **"Make sure that you downloaded this app from Google."** You did, from antigravity.google, so click **Sign in**.
5. The browser says **"You have successfully authenticated"** and asks **"Open Antigravity IDE?"** Click **Open Antigravity IDE**.
6. Back in the app: **Welcome to Antigravity IDE — Success, Continuing…** Click **Next**.

> If a box called **Migrate Settings, Keybindings, and Extensions** pops up, click **Cancel**. It's only for people who used an older version of Antigravity.

**✅ Done when:** the app says **Success**, and you've clicked **Next**.

---

## Step 4 of 8: The setup screens (7 short screens)

| Screen | What to choose |
|---|---|
| **Welcome to Antigravity IDE** | Click **Next**. |
| **Choose setup flow** | **Start fresh**, then **Next**. (The import options are for people moving from another editor.) |
| **Select Theme** | Any look you like. Dark and light both work. Click **Next**. |
| **How do you want to use the Antigravity IDE Agent?** | **Review-driven development** (marked *Recommended*). The AI checks with you before changing things, and reviewing its work is a big part of this course. |
| **Configure Your Editor** | Leave **Normal** and **Recommended** selected. Click **Next**. |
| **Build with Google** | Leave everything **unchecked**. You won't need these. Click **Next**. |
| **Security Notice & Data Use** | Read it (there's more about it just below). The first box (letting Google use your interactions to improve the product) **is checked by default, and it's your choice.** Uncheck it if you prefer. The email box is optional. Click **Next**. |

> **About the security notice.** It warns that AI agents carry risks, including **data exfiltration**: data being sent somewhere you didn't intend. That sounds alarming, and it's meant to make you pause. Here's why the risk exists: an agent can read your files, run commands, and open web pages. A file or web page could contain hidden instructions that trick it into sending your data somewhere. **In this course:**
>
> - Every file is **fictional**. There's nothing real to leak. That's also why the course has one rule: no real patient or research data, ever.
> - The agent **asks before it changes a file or runs a command**, and you can say no. The course shows you how to read those requests.
>
> The warning is honest, and it's a good one to remember if you use agents on real work later. It isn't a reason to stop here.

You'll land on a start screen with two big buttons: **Open Folder** and **Clone Repository**. Leave it open, and get the course next.

**✅ Done when:** you see the start screen with **Open Folder** and **Clone Repository**.

---

## Step 5 of 8: Get the course

1. **[Download the course (ZIP)](https://github.com/dccooper/agentic-psychologist/archive/refs/heads/main.zip).** (Or, on the course's [GitHub page](https://github.com/dccooper/agentic-psychologist), click the green **Code** button, then **Download ZIP**.)
2. **Unzip it.**
   - **Windows:** right-click the ZIP and choose **Extract All…** → **Extract**. (Don't just double-click it. Opening files from inside a ZIP doesn't work.)
   - **Mac:** double-click the ZIP. It unzips into a folder.
3. Optionally, move the unzipped folder somewhere easy to find, like **Documents**.

> **Already use Git?** You can skip the ZIP: click **Clone Repository** on the start screen, paste the course's GitHub address (`https://github.com/dccooper/agentic-psychologist`), and choose where to save it. This needs Git installed on your computer, and Antigravity doesn't include it. If you don't know what Git is, use the ZIP. You'll meet Git at the end of the course.

**✅ Done when:** you have an unzipped folder called `agentic-psychologist-main`.

---

## Step 6 of 8: Open the course in Antigravity

1. On the start screen, click **Open Folder** (or use the menu: **File → Open Folder…**).
2. Choose the unzipped course folder, **`agentic-psychologist-main`**. It's the one that contains `README.md`, `lessons`, and `world`. (If you see just one folder inside another with the same name, go into it.)
3. Antigravity asks whether you trust the authors of the files. Choose **Yes, I trust the authors**. The course needs this so the tutor can work.
4. You should see the course's folders listed in the **Explorer** panel.

**✅ Done when:** the **Explorer** lists the course's folders, including `lessons` and `world`.

---

## Step 7 of 8: Turn off typing suggestions (recommended, 2 minutes)

Antigravity can suggest text *while you type* in a file, shown as grey text you accept with **Tab**. That's useful for programmers, but in this course it muddies a key question: *what did you write, and what did the AI write?* Turn it off for now. The AI tutor still works normally.

1. Open **Antigravity - Settings** (bottom-right corner of the window, or the gear icon at the top right). ⚠️
2. Find the **Tab** section and turn **off**: **Autocomplete**, **Supercomplete**, **Tab-to-Jump**, and **Tab-to-Import**. ⚠️
3. You can turn them back on any time after the course.

If you can't find these, skip this step and tell the tutor. It isn't required.

**✅ Done when:** the four **Tab** settings are off (or you've skipped this step, which is fine).

---

## Step 8 of 8: Start the course

1. Find the **agent panel**. It's usually already open on the right, with a message box that says *"Ask anything, @ to mention, / for actions"*. If it isn't, press **Ctrl+L** (Windows) or **Cmd+L** (Mac).
2. Type **`/sta`**, then press **Tab**. Antigravity fills in the rest, and you'll see a small **start-course** tag in the message box.
3. Press **Enter**.

> **Use Tab for every course command.** Typing a command out in full doesn't always work (testers on a Mac found `/start-course` did nothing until they used Tab). Type the slash and the first few letters, then press **Tab**. If you do type it out and nothing happens, the tutor should still understand *"start the course"* in plain words.

**✅ Done when:** the tutor welcomes you. That's setup finished, and the tutor takes it from here. 🎓

### Two things to know before you start

**Replies can take a minute or two.** That's normal, especially on the free plan and on older computers. While the AI is working, the agent panel shows its activity: a **Working…** line, or lines like *"Analyzed README.md"*. As long as you see that, wait. **Don't refresh, close the window, or send the message again.** If nothing has changed for five minutes, see [If something goes wrong](#if-something-goes-wrong).

**The AI asks before it changes anything.** When it wants to edit a file, buttons appear: **Accept** and **Reject** (or **Accept all** / **Reject all** above the message box). **Accept** keeps that one change, to the file named right there. **Reject** undoes it. Neither one gives the AI permission for anything else, and it's always safe to say no. If you're unsure, ask the tutor *"What exactly would I be accepting?"* The first lesson walks you through it.

---

## If something goes wrong

- **I downloaded the wrong app** (there's no list of files on one side and no **File → Open Folder** menu): you probably got the **Antigravity App**. Go back to step 1 and get **Antigravity IDE (Standalone)**, near the bottom of the page. You can uninstall the other one.
- **Sign-in fails with a university account:** try a personal Google account.
- **The browser didn't switch back to the app after signing in:** click **Open Antigravity IDE** in the browser's pop-up, or **Click here** on the "successfully authenticated" page.
- **I can't find the app after installing:** on Windows, press the Windows key and type *Antigravity IDE*. (Make sure it says **IDE**. Plain "Antigravity" is the other app.)
- **The tutor doesn't seem to know about the course:** make sure you opened the course folder itself (step 6.2), not the ZIP or a folder above it.
- **Typing `/start-course` does nothing:** delete it, type `/sta`, and press **Tab**. Or just type *start the course* and press **Enter**.
- **A reply is taking forever:** a minute or two is normal. If the agent panel hasn't changed in five minutes, start a new conversation (the **+** at the top of the agent panel) and type `/sta` + **Tab** again. Your place in the course is saved in a file, so nothing is lost.
- **A skill you just made doesn't show up when you type `/`:** new skills only appear in a **new conversation** (the **+**). If it still isn't there, close Antigravity completely (on a Mac, **Antigravity → Quit**, or Cmd+Q) and open it again. If the course folder doesn't reopen, use **File → Open Recent**.
- **The AI stops replying, or says you've reached a limit:** the free plan has a usage limit that resets weekly. Your progress is saved, so you can:
  - **Wait for the reset** and pick up where you left off with `/sta` + **Tab**.
  - **Try another model.** The model's name is shown in the message box (for example *Gemini … Flash*). Click it to see what else your plan offers. A different model may still have room.
  - **Upgrade**: a paid Google plan raises the limit. The course doesn't require it.
