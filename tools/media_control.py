from core.audio_engine import say
import pyautogui

def pause_resume():
    try:
        pyautogui.press('playpause')
        return True, f"Done"
    except Exception as e:
        return False, f"Unable to do it."

def volume_down():
    try:
        for _ in range(5):
            pyautogui.press('volumedown')
        return True, f"Done"
    except Exception as e:
        return False, f"Unable to do it."

def volume_up():
    try:
        for _ in range(5):
            pyautogui.press('volumeup')
        return True, f"Done"
    except Exception as e:
        return False, f"Unable to do it."

def play_next():
    try:
        pyautogui.press('nexttrack')
        return True, f"Done"
    except Exception as e:
        return False, f"Unable to do it."

def play_previous():
    try:
        pyautogui.press('previoussong')
        return True, f"Done"
    except Exception as e:
        return False, f"Unable to do it."