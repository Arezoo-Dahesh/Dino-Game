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


# ------ After 5 seconds, the dino starts jumping (with space key) ------
time.sleep(5)
for i in range(1,500):
    pyautogui.press('space')

