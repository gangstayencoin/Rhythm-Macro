from pynput.keyboard import Controller
import time

keyboard = Controller()

def press_keys(keys, hold_time=0.003):
    for k in keys:
        keyboard.press(k)
    time.sleep(hold_time)
    for k in keys:
        keyboard.release(k)
