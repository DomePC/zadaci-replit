import keyboard
import pyautogui
import win32api
import win32con
import time
import os

profile_img = 'Autostarter1.0\\img\\profile.png'
start = 'Autostarter1.0\\img\\start.png'
print("Waiting for game session...")



def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print("Waiting to start:",timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

while not keyboard.is_pressed('ENTER'):
    first_image = pyautogui.locateCenterOnScreen(profile_img, region=(0,0,1920,1080), grayscale=True, confidence=0.99)
    second_image = pyautogui.locateCenterOnScreen(start, region=(0,0,1920,1080), grayscale=True, confidence=0.7)

    if first_image is not None:
        os.system('CLS')
        pyautogui.moveTo(first_image) 
    countdown(300)
    os.system('CLS')
    
    if second_image is not None:
        pyautogui.moveTo(second_image)
        click()
    print('Game starting...')

    time.sleep(100)

    os.system('CLS')