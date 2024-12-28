
# Auto Accept Script

This Python script automates the process of detecting a button (represented by an image) on the screen and clicking it. It utilizes the `pyautogui` library for screen automation and the `tkinter` library for a basic graphical user interface (GUI) to start and stop the automation process.

 Requirements

- Python 3.x
- `pyautogui` library
- `tkinter` library (usually comes pre-installed with Python)

You can install `pyautogui` using pip:

```bash
pip install pyautogui
```

 How It Works

The script runs an auto-accept function that:
1. Continuously checks for an image (e.g., a button) on the screen.
2. If the image is found, it clicks the center of the image.
3. Logs the status in a GUI window, indicating whether the button was found and accepted or not.

A `Start` button begins the process, and a `Stop` button halts it. The script uses threading to ensure that the GUI remains responsive while the script is running.

 Features

- **Auto Accept Button**: Detects and clicks on a specified image on the screen.
- **Logs**: Provides real-time logging of the script's actions in the GUI.
- **Start/Stop Control**: Easily start or stop the automation process with buttons.

 Use Case: Game Match Acceptance

This script is particularly useful for games like **League of Legends** or other multiplayer online games where you need to click an "Accept" button to enter a match. These games often require players to manually click a button to confirm their participation in a match. If you're AFK or busy, the script will automatically accept the match for you, ensuring you don't miss any opportunities to play.

 Usage

1. **Set the Image Path**: Replace the placeholder in the `image_path` variable with the path to the image you want the script to find and click.
    ```python
    image_path = r"IMPAGE PATH HERE"
    ```

2. **Run the Script**: Execute the script. The GUI window will open with buttons for controlling the process.

3. **Start the Automation**: Click the "Start Auto Accept" button to begin the image search and click automation.

4. **Stop the Automation**: Click the "Stop" button to stop the script.

 Example

- **Image Path**: Ensure that the image file you are using is visible on the screen and has a recognizable and unique feature for the script to locate it.

 Limitations

- The `confidence` parameter in `pyautogui.locateCenterOnScreen` can be adjusted to control how closely the image must match, but very low or very high values might cause detection failures.
- The script relies on the button image being visible and in focus on the screen.
