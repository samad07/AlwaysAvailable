import keyboard
import time
time.sleep(10)
while True:
    keyboard.write('brown fox')
    time.sleep(3)
    keyboard.press_and_release('ctrl+a, space')
    time.sleep(20)