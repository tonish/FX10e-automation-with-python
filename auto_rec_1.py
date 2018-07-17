import autoit
import pyautogui
import ctypes
import win32con
import send_mail
import time
import os

def setWallpaperWithCtypes(image):
    cs = ctypes.c_buffer(image)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 1)

# lumoscanner loads on startup or load it 
# pyautogui.click(x= 269, y = 1059) # lunch LUMU scanner
num_of_dirs = len(os.listdir(r'D:\Chamama\OneDrive - mail.tau.ac.il\Chamama'))
# connect to camera
autoit.win_activate("Scanner")
time.sleep(2)
#pyautogui.click(x = 1660, y = 72) # press setup button
#time.sleep(2)
#pyautogui.click(x = 1085, y = 284) # press connect camera button
#time.sleep(3)

# conect to motor 
#pyautogui.click(x = 1085, y = 284) # change the coordinates after camera connects # press connect camera button 
#time.sleep(3)
# move to white reference
pyautogui.click(x = 1123, y = 71) # press adjust button
time.sleep(2)
# change the coordinates to 0 degrees
pyautogui.moveTo(914,236) 
pyautogui.mouseDown()
time.sleep(5)
pyautogui.mouseUp()
 # change the coordinates to reach whith ref
pyautogui.click(x = 1209, y = 794)# press go to 84 degrees
time.sleep(5)

## adjust configuration
## set the start with maximum exposure time
num = 39
pyautogui.click(x = 233, y = 209) # press exposure time button ,make exposure time defult 39
time.sleep(1)
pyautogui.tripleClick(x = 233, y = 209)
autoit.send(str(num))
pyautogui.click(x = 236, y = 304) # press apply
time.sleep(15)

while True:
    try: 
        pyautogui.screenshot(r'C:\Users\user\Documents\tmp.jpg')
        time.sleep(2)
        image = r'C:\Users\user\Documents\tmp.jpg'
        time.sleep(2)
        setWallpaperWithCtypes(image)
        time.sleep(2)
        autoit.pixel_search(586,116,295,534, 0xFF0000) # check if there are red pixels
        time.sleep(2)
        print "found a red pixel" # remove later
        num = num-3
        pyautogui.click(x = 233, y = 209) # press exposure time button ,make exposure time defult 39
        time.sleep(2)
        pyautogui.tripleClick(x = 233, y = 209)
        autoit.send(str(num))
        pyautogui.click(x = 236, y = 304) # press apply
        time.sleep(15)
    except:
        print 'broken loop'
        break
##
## 
## record
pyautogui.click(x = 1179, y = 145) # press record
time.sleep(180)
# send e-mail
if len(os.listdir(r'D:\Chamama\OneDrive - mail.tau.ac.il\Chamama')) > num_of_dirs:
    send_mail.send_mail()
    time.sleep(2)
#
