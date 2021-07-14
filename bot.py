import pyautogui
import time
"""
Not a pyautogui user, but on Mojave, 
there's a new security feature where you must explicitly allow applications to use your mouse/keyboard. 
Have a look in 
Security Preferences > Security & Privacy > Privacy > Accessibility
- 
you might have to allow your terminal application in the list.
"""
time.sleep(3)
print(pyautogui.position())
# pyautogui.click(500, 500)
# pyautogui.typewrite('Hello world!', interval=0.1)

# pyautogui.moveTo(4669,90)
# pyautogui.dragTo(button='left')

pyautogui.click(217,80)