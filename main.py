from pyautogui import *
import time
import keyboard
import pyautogui
import win32api, win32con


# You need to change those numbers based on your tiles's 's position. You can use pyautogui to display your mouse position with
# pyautogui.displayMousePosition()


#FIRST COLUMNS COORDINATES = (320, 820)
#SECOND COLUMNS COORDINATES = (420, 820)
#THIRD COLUMNS COORDINATES = (520, 820)
#FOURTH COLUMNS COORDINATES = (620, 820)

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)  # a click that goes too fast might cause problems
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(320, 680)[0] == 0: # we only verify if the red value is 0, because there is no point on verifying the others also
        click(320, 680)

    if pyautogui.pixel(420, 680)[0] == 0:
        click(420, 680)
    
    if pyautogui.pixel(520, 680)[0] == 0:
        click(520, 680)
        
    if pyautogui.pixel(620, 680)[0] == 0:
        click(620, 680)