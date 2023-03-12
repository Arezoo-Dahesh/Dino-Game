# ------ Import libraries ------
import webbrowser
import pyautogui
from PIL import Image, ImageGrab 
import cv2
import time
import numpy as np
# importmatplotlib.pyplot as plt

# ------ Get current mouse position ------
# print(pyautogui.position())

# top-left
# Point(x=553, y=349)

# bottom-right
# Point(x=1311, y=443)

               
# ------ Define functions ------
def take_screenshot():
    image = ImageGrab.grab(bbox =(553, 349, 1311, 443)).convert('L')
    img = np.array(image)
    # binarize image
    _, thresh_image = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
    # plt.imshow(thresh_image)
    return thresh_image


# ------ Open URL ------
# 1
webbrowser.open('http://chromedino.com/') 
                          
# 2
# webbrowser.register('chrome', None, 
#                     webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
# webbrowser.get('chrome').open_new('http://chromedino.com/')

                 
# ------ After 10 seconds, start game ------
time.sleep(10)
pyautogui.press('space')


time.sleep(1)
for i in range(1,1200):
    image = take_screenshot()
    sumOfColumns = list(np.sum(image, axis=0))
    AVG = np.mean(sumOfColumns[200:270])
    if AVG < 22950:
        pyautogui.press('space')

