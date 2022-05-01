import keyboard
import pyautogui
import win32api
import win32con

agent_list = ['Instalocker1.0\\agents\\astra.png', 'Instalocker1.0\\agents\\breach.png', 'Instalocker1.0\\agents\\brimstone.png', 'Instalocker1.0\\agents\\chamber.png', 'Instalocker1.0\\agents\\cypher.png', 'Instalocker1.0\\agents\\fade.png', 'Instalocker1.0\\agents\\jett.png', 'Instalocker1.0\\agents\\kayo.png', 'Instalocker1.0\\agents\\killyoj.png', 'Instalocker1.0\\agents\\neon.png', 'Instalocker1.0\\agents\\omen.png', 'Instalocker1.0\\agents\\pheonix.png', 'Instalocker1.0\\agents\\raze.png', 'Instalocker1.0\\agents\\reyna.png', 'Instalocker1.0\\agents\\sage.png', 'Instalocker1.0\\agents\\skye.png', 'Instalocker1.0\\agents\\sova.png', 'Instalocker1.0\\agents\\viper.png', 'Instalocker1.0\\agents\\yoru.png']


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0 ,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

select_agent = input("Enter what agent you want to instalock: ")

while not keyboard.is_pressed('ENTER'):
    
    for i in range(19):
        agent_selection = agent_list[i].endswith(select_agent.lower()+".png")
        if agent_selection is True:
            selected_agent = agent_list[i]
            
    
    first_image = pyautogui.locateCenterOnScreen(selected_agent,region=(0, 0, 1920, 1080), grayscale=True, confidence=0.99)
    second_image = pyautogui.locateCenterOnScreen('Instalocker1.0\\lock.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.85)

    if first_image is not None:
        pyautogui.moveTo(first_image)
        click()
    if second_image is not None:
        pyautogui.moveTo(second_image)
        click()
    elif first_image is not None or second_image is not None:
        print("You selected",select_agent)

