import pyautogui

pyautogui.FAILSAFE = False
import ctypes

user  = ctypes.windll.user32
width = user.GetSystemMetrics(0)
height = user.GetSystemMetrics(1)

pyautogui.click(0,height)
print("start button  clicked")
pyautogui.typewrite(" salesmate + ",0.2)
print("salesmate+Types")
pyautogui.press("enter",1,10)
print("Salesmate+ software opened")
pyautogui.press("c")
pyautogui.press("c")
pyautogui.press(["alt","c"])
pyautogui.press(["ctrl","a"])
pyautogui.press("tab",2,0.1)
pyautogui.typewrite("irshath")
pyautogui.press("tab")
pyautogui.typewrite("ahamed")
pyautogui.press("tab")
pyautogui.typewrite("irshath ahamed")
pyautogui.press("tab")
pyautogui.typewrite("madurai ")
pyautogui.press("tab")
pyautogui.typewrite("1234567890")
pyautogui.press("tab")
pyautogui.typewrite("ahamedirshath123@gmail.com")
pyautogui.press("tab", 9,0.1)
pyautogui.press("enter") 
pyautogui.press("enter")  