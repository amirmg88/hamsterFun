#@Amirmgo -- TelegramID
import time
import random
import pyautogui

while True:
    time.sleep(2)
    p = (pyautogui.position())
    print(p)
    print(type(p))

    m = input("Position?")
    if m == "1":
        x_1 = p.x
        y_1 = p.y

    if m == "2":
        x_2 = p.x
        y_2 = p.y

    if m == "3":
        x_3 = p.x
        y_3 = p.y

    if m == "4":
        x_4 = p.x
        y_4 = p.y
    if m == "fin":
        break
    else:
        continue

i = 0
delay = random.uniform(0.20, 0.30)
while True:
    time.sleep(delay)
    x_main = random.uniform(x_1, x_2)
    y_main = random.uniform(y_3, y_4)
    pyautogui.click(x=x_main, y=y_main)
    i = i + 1
    if i == 100:
        #i = 0
        delay = random.uniform(0.20, 0.30)
    if i == 4000:
        i = 0
        time.sleep(800)
        delay = random.uniform(0.20, 0.30)
