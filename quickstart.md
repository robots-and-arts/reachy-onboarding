# Quickstart Guide

Follow this guide to get your Reachy Mini up and running, either on real hardware or in simulation.

## 1. Download Reachy Mini Control

**Reachy Mini Control** is the desktop app that acts as the command center for your robot. It includes visualization tools, an app launcher, and system settings, with no command line required.

- 👉 [Download from the official website](https://hf.co/reachy-mini/#/download) (recommended for Windows, macOS, and Linux)
- Alternative: [GitHub Releases](https://github.com/pollen-robotics/reachy-mini-desktop-app/releases) (for specific versions)

**✨ Auto-update:** Once installed, open the app. It automatically checks for and installs updates for both the app and the robot's internal software.

> **⚠️ Compatibility:** On ARM64 systems (DGX, Jetson, Surface, etc.) and unusual Linux distributions, the desktop app may not work. In that case, use the [Python SDK](https://huggingface.co/docs/reachy_mini/SDK/readme) directly (see [Alternative: Run the daemon from the command line](#alternative-run-the-daemon-from-the-command-line)). It is a fully supported way to control your robot.

## 2. Connect your robot

1. Connect your **Reachy Mini Lite** to your computer via USB.
2. Open **Reachy Mini Control** and allow any permissions your operating system requests.
3. Select **Reachy Mini Lite** in the app.

✅ **Verification:** The app shows real-time information about your robot. If you see it, you are ready.

## 3. Explore apps

1. Log in with your Hugging Face account.
2. Go to the **Applications** tab and click **Discover Apps** to browse compatible apps from Hugging Face Spaces.
3. Click **Install** on an app, then click **Start ▶️** to run it.

For more, see the [Usage Guide](https://huggingface.co/docs/reachy_mini/platforms/reachy_mini_lite/usage).

## 4. Your first script

> **⚠️ Important:** Keep Reachy Mini Control open and connected while running scripts. The app runs the background service that your code connects to.

Make sure the Reachy Mini SDK is installed and your Python virtual environment is activated (see the [installation guide](installation.md)). Remember to activate it every time you open a new terminal.

Create a file called `hello.py`:

```python
from reachy_mini import ReachyMini

# Connect to the running daemon
with ReachyMini() as mini:
    print("Connected to Reachy Mini!")

    # Wiggle antennas
    print("Wiggling antennas...")
    mini.goto_target(antennas=[0.5, -0.5], duration=0.5)
    mini.goto_target(antennas=[-0.5, 0.5], duration=0.5)
    mini.goto_target(antennas=[0, 0], duration=0.5)

    print("Done!")
```

Run it in a new terminal:

```bash
python hello.py
```

🎉 If everything went well, your robot should now wiggle its antennas!

## Alternative: Run the daemon from the command line

If you can't use the desktop app, or you want a headless setup, start the daemon manually and keep that terminal open.

**Reachy Mini Lite (USB)**

- Windows (PowerShell):
```bash
  uv run --with "reachy-mini==1.2.6rc2" reachy-mini-daemon
```
- Linux / macOS:
```bash
  uv run reachy-mini-daemon
```

**Simulation (no robot needed)**

- Windows (PowerShell):
```bash
  uv run --with "reachy-mini==1.2.6rc2" reachy-mini-daemon --sim
```
- Linux / macOS:
```bash
  uv run reachy-mini-daemon --sim
```

✅ **Verification:** Open [http://localhost:8000](http://localhost:8000). If you see the Reachy Dashboard, you are ready. Then continue with [Your first script](#4-your-first-script).
