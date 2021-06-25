import time
import pyautogui
import PIL
import os
from tkinter.filedialog import *
a=0
timemoment = input("What is the interval between 2 screenshots in seconds:")
try:
    timemomento = float(timemoment)
except Exception:
    print("Please input a floating point number")
maximum = input("What is the maximum amount of screenshots: ")   
try:
    maxmomento = int(maximum)
except Exception:
    print("Please input a intiger")
print("Select a save directory: ")  
time.sleep(1)
path = askdirectory()
while a<=maxmomento:
    screenshot = pyautogui.screenshot()
    screenshot.save(path+"/"+str(a)+"unc.png")

    img = PIL.Image.open(path+"/"+str(a)+"unc.png")
    height, width = img.size

    img = img.resize((height, width) , PIL.Image.ANTIALIAS)
    img.save(path+"/"+str(a)+".png")

    os.remove(path+"/"+str(a)+"unc.png")
    a+=1
    time.sleep(timemomento)