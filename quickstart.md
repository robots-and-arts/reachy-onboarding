# Quickstart Guide

Follow this guide to get your Reachy Mini up and running, either on real hardware or in simulation.

## 1. Prerequisites

Make sure you have installed Reachy Mini on your computer following our [installation guide](installation.md). 

> **💡 Important:** Ensure you have created and activated your Python virtual environment. **Remember to activate it every time you open a new terminal!** In order to know if your virtual environment is active, you should see (<your_env_name>) at the start of a new line in your terminal.


## 2. Ensure the Robot Server is running (Daemon)

The **Daemon** is a background service that handles the low-level communication with motors and sensors. It must be running for your code to work.

* **On Reachy Mini Lite (connected via USB to your computer)**:
  - If you are using a **Windows** system, open a terminal/powershell and run :
  ```bash
  uv run --with "reachy-mini==1.2.6rc2" reachy-mini-daemon
  ```
  - If you are using a **Linux** or a **Mac** system, open a terminal and run :
  ```bash
  uv run reachy-mini-daemon
  ```
* **For Simulation (No robot needed)**:
  - On a **Windows** system, open a terminal/powershell and run:
  ```bash
  uv run --with "reachy-mini==1.2.6rc2" reachy-mini-daemon --sim
  ```
  - On a **Linux** or **Mac** system, open a terminal and run:
  ```bash
  uv run reachy-mini-daemon --sim
  ```

✅ **Verification:** Open [http://localhost:8000](http://localhost:8000) in your browser. If you see the Reachy Dashboard, you are ready!

## 3. Your First Script

> **⚠️ Important:** Keep the daemon terminal open and running! The daemon must stay active for your robot to work.

### Create your Python script

**Step 1:** Open a new terminal window

**Step 2:** Create a new file called `hello.py` and copy-paste the following code into it:

```python
from reachy_mini import ReachyMini

# Connect to the running daemon
with ReachyMini() as mini:
    print("Connected to Reachy Mini! ")
    
    # Wiggle antennas
    print("Wiggling antennas...")
    mini.goto_target(antennas=[0.5, -0.5], duration=0.5)
    mini.goto_target(antennas=[-0.5, 0.5], duration=0.5)
    mini.goto_target(antennas=[0, 0], duration=0.5)

    print("Done!")
```

**Step 3:** Save the file and run your script:

In your new terminal, run:
```bash
python hello.py
```
⚠️ Ensure that you are running the script while your virtual environment is running.

🎉 If everything went well, your robot should now wiggle its antennas!
