import ctypes
import win32con
import pyautogui

def setWallpaperWithCtypes(image):
    cs = ctypes.c_buffer(image)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 1)
    
if __name__ == "__main__":
    autoit.win_activate("Scanner")
    pyautogui.screenshot(r'C:\Users\user\Documents\tmp.jpg')
    image = r'C:\Users\user\Documents\tmp.jpg'
    setWallpaperWithCtypes(image)