import time
import pyautogui
import cv2
import numpy as np
import pygetwindow as gw
import logging
from datetime import datetime
import hashlib
import os
import argparse
import AppKit
from Quartz.CoreGraphics import CGEventCreateMouseEvent, kCGEventLeftMouseDown, kCGEventLeftMouseUp, kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
import Quartz
import logging
import subprocess

class ScreenActivityTracker:
    def __init__(self, log_dir='activity_logs'):
        """
        Initialize the Screen Activity Tracker

        Args:
            log_dir (str): Directory to store activity logs
        """
        self.log_dir = log_dir
        self.last_screenshot = None
        self.setup_logging()

    def setup_logging(self):
        """
        Configure logging for tracking activities
        """
        os.makedirs(self.log_dir, exist_ok=True)
        log_filename = f'{self.log_dir}/screen_activity_{datetime.now().strftime("%Y%m%d")}.log'
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def capture_screenshot(self):
        """
        Capture screenshot and return as numpy array

        Returns:
            numpy.ndarray: Screenshot image
        """
        screenshot = pyautogui.screenshot()
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    def detect_screen_changes(self, threshold=0.01):
        """
        Detect significant changes in screen content

        Args:
            threshold (float): Sensitivity of change detection

        Returns:
            bool: True if significant change detected, False otherwise
        """
        current_screenshot = self.capture_screenshot()

        if self.last_screenshot is None:
            self.last_screenshot = current_screenshot
            return True

        # Compute difference between current and last screenshot
        diff = cv2.absdiff(self.last_screenshot, current_screenshot)
        change_percentage = np.sum(diff > 30) / (diff.shape[0] * diff.shape[1])

        is_changed = change_percentage > threshold

        if is_changed:
            self.last_screenshot = current_screenshot

        return is_changed

    def get_active_window_info(self):
        """
        Retrieve information about the currently active window on macOS using the Accessibility API.
        
        Returns:
            dict: Window details including title, dimensions, or None if unavailable
        """
        try:
            # Using Accessibility API to get the active window
            app = AppKit.NSWorkspace.sharedWorkspace()
            active_app = app.frontmostApplication()

            # Get the active app's window using Accessibility API (AXUIElement)
            ax_app = Quartz.CGEventCreateMouseEvent(active_app, Quartz.kCGEventMouseMoved, (0, 0), Quartz.kCGEventLeftMouseDown)
            
            window_title = active_app.localizedName()

            # Return window details (for this example, assuming we can get dimensions)
            return {
                'title': window_title,
                'size': (1000, 800),  # Placeholder for actual dimensions
                'position': (0, 0)    # Placeholder for actual position
            }

        except Exception as e:
            logging.error(f"Could not retrieve active window: {e}")
            return None
    def get_window_position_size():
        try:
            script = '''
            tell application "System Events"
                set frontApp to name of the first application process whose frontmost is true
                tell application frontApp
                    set windowPosition to the position of the front window
                    set windowSize to the size of the front window
                end tell
            end tell
            '''
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            window_info = result.stdout.strip().split(',')
            position = tuple(map(int, window_info[0].split()))
            size = tuple(map(int, window_info[1].split()))
            return {'position': position, 'size': size, 'title': frontApp}
        except Exception as e:
            logging.error(f"Error retrieving window info: {e}")
            return None    
    def track_mouse_movement(self, duration=60, interval=1):
        """
        Track mouse movements over a specified duration

        Args:
            duration (int): Total tracking time in seconds
            interval (int): Time between position checks

        Returns:
            list: Mouse position history
        """
        mouse_positions = []
        start_time = time.time()

        while time.time() - start_time < duration:
            mouse_positions.append({
                'timestamp': time.time(),
                'position': pyautogui.position()
            })
            time.sleep(interval)

        return mouse_positions

    def log_activity(self):
        """
        Comprehensive activity logging
        """
        # Screen change detection
        if self.detect_screen_changes():
            logging.info("Screen content changed")

        # Active window tracking
        window_info = self.get_active_window_info()
        if window_info:
            logging.info(f"Active Window: {window_info['title']}")

        # Optional: Log mouse movements
        # Uncomment if you want to track mouse movements
        # mouse_log = self.track_mouse_movement(duration=10)
        # logging.info(f"Mouse Movements: {mouse_log}")

    def start_continuous_tracking(self, interval=5):
        """
        Start continuous activity tracking

        Args:
            interval (int): Time between tracking checks
        """
        try:
            while True:
                self.log_activity()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Tracking stopped by user.")
        except Exception as e:
            logging.error(f"Tracking error: {e}")


# Example usage
if __name__ == "__main__":
    tracker = ScreenActivityTracker()
    tracker.start_continuous_tracking()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Screen Activity Tracker")
    parser.add_argument("--log_dir", type=str, default="activity_logs", help="Directory to store logs")
    parser.add_argument("--interval", type=int, default=5, help="Time interval between activity checks")
    parser.add_argument("--log_level", type=str, default="INFO", help="Set logging level (INFO, DEBUG, ERROR)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), None))
    tracker = ScreenActivityTracker(log_dir=args.log_dir)
    tracker.start_continuous_tracking(interval=args.interval)