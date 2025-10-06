import pyautogui
from config import jump_key

def jump():
    pyautogui.press(jump_key)
    print("✅ Dino jumped")