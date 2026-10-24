# Setup: Getting Ready (about 15 minutes)

You'll install a free app called **Antigravity IDE**, sign in with a Google account, and open the course in it. After that, the course teaches itself: an AI tutor inside the app takes over.

> **You don't need any technical experience.** If something here doesn't match your screen, that's normal (apps update often). Take your best guess, and once the tutor is running, tell it what happened.

<!-- Authors: steps marked ⚠️ weren't captured in testing yet. Verify them on the next fresh install (QA pass 2). -->

## 1. Download the right app

1. Go to **https://antigravity.google/download**.
2. ⚠️ **Careful: the first download on that page is the wrong one.** The page lists several products. The first, **Antigravity App**, is a different app. Skip it. Also skip **Antigravity CLI**.
3. Scroll down to **Antigravity IDE (Standalone)**. This is the one you want.
4. Click the button for your computer:
   - **Windows:** **Download for x64** (almost all Windows PCs). Choose ARM64 only if your laptop has a Snapdragon / ARM chip. To check, go to **Settings → System → About → System type**.
   - **Mac:** **Download for Apple Silicon** if your Mac has an M1, M2, M3 or newer chip. Choose **Download for Intel** for older Macs. To check, open **Apple menu → About This Mac → Chip / Processor**.

## 2. Install it

Open the file you downloaded (usually in your **Downloads** folder) and follow the installer. On a Mac, drag Antigravity into **Applications**.

## 3. Sign in with Google ⚠️

1. Open **Antigravity IDE**. It will ask you to sign in with Google, usually by opening your web browser.
2. Choose a Google account and approve the sign-in. **A personal Google account is simplest.** University Google accounts sometimes block new apps. (The course never uses real patient or research data, so a personal account is fine for it.)
3. Go back to the app. You should see **Welcome to Antigravity IDE** and **Success, Continuing…** Click **Next**.

## 4. The setup screens (7 short steps)

| Screen | What to choose |
|---|---|
| **Welcome to Antigravity IDE** | Click **Next**. |
| **Choose setup flow** | **Start fresh**, then **Next**. (The import options are for people moving from another editor.) |
| **Select Theme** | Any look you like. Dark and light both work. Click **Next**. |
| **How do you want to use the Antigravity IDE Agent?** | **Review-driven development** (marked *Recommended*). The AI checks with you before changing things, and reviewing its work is a big part of this course. |
| **Configure Your Editor** | Leave **Normal** and **Recommended** selected. Click **Next**. |
| **Build with Google** | Leave everything **unchecked**. You won't need these. Click **Next**. |
| **Security Notice & Data Use** | Read it. The first box (letting Google use your interactions to improve the product) **is checked by default, and it's your choice.** Uncheck it if you prefer. The email box is optional. Click **Next**. |

## 5. Get the course

1. On the course's GitHub page, click the green **Code** button, then **Download ZIP**.
2. **Unzip it.**
   - **Windows:** right-click the ZIP and choose **Extract All…** → **Extract**. (Don't just double-click it. Opening files from inside a ZIP doesn't work.)
   - **Mac:** double-click the ZIP. It unzips into a folder.
3. Optionally, move the unzipped folder somewhere easy to find, like **Documents**.

## 6. Open the course in Antigravity

1. In Antigravity: **File → Open Folder…**
2. Choose the unzipped course folder. It's the one that contains `README.md`, `lessons`, and `world`. (If you see just one folder inside another with the same name, go into it.)
3. ⚠️ If asked whether you trust the authors of the files, choose **Yes, I trust the authors**. The course needs this so the tutor can work.
4. You should see the course's folders listed in the **Explorer** panel.

## 7. Start the course

1. Open the **agent panel**: press **Ctrl+L** (Windows) or **Cmd+L** (Mac). Or click **Code with Agent** in the middle of the window.
2. In the message box (it says *"Ask anything, @ to mention, / for actions"*), type:

   ```
   /start-course
   ```

   and press **Enter**.

The tutor takes it from here. Replies can take a few seconds, so be patient. 🎓

## If something goes wrong

- **I downloaded the wrong app** (it doesn't look like a code editor with a file list): go back to step 1 and get **Antigravity IDE (Standalone)**. You can uninstall the other one.
- **Sign-in fails with a university account:** try a personal Google account.
- **The tutor doesn't seem to know about the course:** make sure you opened the course folder itself (step 6.2), not the ZIP or a folder above it.
