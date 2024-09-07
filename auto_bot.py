import pyautogui
import random
import time

pyar = ["zargey", "janan", "qurban", "baby","wifey","begum","bacha"]
for i in range(50):
    message = f'i love you {random.choice(pyar)}'
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(0.5)
