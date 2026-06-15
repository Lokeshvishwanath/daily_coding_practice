# Day 49 - Screenshot Capture Tool

import pyautogui
from datetime import datetime

class ScreenshotTool:

    def take_screenshot(self):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"screenshot_{timestamp}.png"

        screenshot = pyautogui.screenshot()

        screenshot.save(file_name)

        print(f"\nScreenshot saved as '{file_name}'")


def main():

    print("===== SCREENSHOT CAPTURE TOOL =====")

    tool = ScreenshotTool()

    input("Press ENTER to capture screenshot...")

    try:

        tool.take_screenshot()

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()