import autoit
import pyautogui
import ctypes
import win32con


def setWallpaperWithCtypes(image):
    cs = ctypes.c_buffer(image)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 1)

image = r'C:\Users\user\Documents\tmp.jpg'
setWallpaperWithCtypes(image)
#autoit.run("mspaint.exe")
#autoit.win_activate('Untitled - Paint')
pixelcolor = autoit.pixel_get_color(481,577)
print pixelcolor
try:
    pixarray = autoit.pixel_search(874,116,295,534, 0xFF0000)
    print pixarray[0], pixarray[1]
    print "red!!"
except:
    print "none"
    
    
    