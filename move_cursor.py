import random
import pyautogui as pgui


pgui.PAUSE = 5
pgui.FAILSAFE = False
width, height = pgui.size()

while 1:
    # x = random.randrange(10, width-10)
    # y = random.randrange(10, heght-10)
    # pgui.moveTo(x, y, duration=0.30)
    pgui.click(width - 2, height - 2)
# pgui.moveTo(x, y)
