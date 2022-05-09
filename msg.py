mport pyautogui as pt
import time

limit = input("enter limit:")
message = input("message: ")
i = 0
time.sleep(10)

while i<int(limit):
    
    pt.typewrite(message)
    pt.press("enter")


 
    i+=1

