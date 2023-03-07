# ------ Import libraries ------
import webbrowser
import pyautogui
import time


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
           