import autoit
import pyautogui
import send_mail_9_5_2018 as send_mail
import time
import datetime
import os
import pyscreeze
# import PIL.ImageGrab as imagegrab
import numpy as np
import shutil
import glob
import change_ethernet
import subprocess


'''
x=312, y=243   -----------------------  x=894,y=243
              |                       |
              |                       |
              |                       |
x= 312, y=500  -----------------------  x= 894, y=500
'''


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        t -= 1


def move_camera(t=1):
    pyautogui.click(x=366, y=748)  # press arduino button
    time.sleep(1)
    # pyautogui.click(x = 748, y = 264)#press arduino button
    pyautogui.click(x=393, y=77) # open monitor
    time.sleep(1)
    pyautogui.click(x=462, y=189)  # open monitor
    time.sleep(2)
    pyautogui.press('0')  # press to defult the console
    pyautogui.press('enter')  # press enter
    time.sleep(1)
    pyautogui.press('1')  # press 1
    time.sleep(1)
    pyautogui.press('enter')  # press enter
    time.sleep(t)  # wait t sec
    pyautogui.press('0')  # press to defult the console
    pyautogui.press('enter')  # press enter
    pyautogui.hotkey('alt', 'f4')  # close monitor


def search_red(im):
    booll = False
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (arr[i, j] == [255, 0, 0]).all():
                booll = True
    return booll


def check_start():
    pyautogui.click(x=1195, y=65)  # press adjust button
    time.sleep(1)
    im1 = pyscreeze.screenshot().convert('L')
    im1 = np.array(im1)
    pyautogui.click(x=1095, y=66)  # press setup
    time.sleep(1)
    pyautogui.click(x=796, y=279)  # connect LUMU recorder
    time.sleep(15)
    pyautogui.click(x=1195, y=65)  # press adjust button
    time.sleep(1)
    im2 = pyscreeze.screenshot().convert('L')
    im2 = np.array(im2)
    if (im1 == im2).all():
        return False
    else:
        return True


"""-------------------------------------------------------------------"""

send_mail.send_mail('start')
time.sleep(2)
f = open(r"D:\logger.txt", "w+")
f.write('line 87')


#load Lumorecorder
pyautogui.click(x= 319, y = 745) # lunch LUMU recorder
time.sleep(2)

while check_start() == False:
    print (check_start())
    change_ethernet.change_ethernet()
    pyautogui.click(x=972, y=279)  # disconnect LUMU recorder
    time.sleep(2)
    check_start()



num_of_dirs = len(os.listdir(r'D:\Data'))

f.write('line 105')

# adjust configuration
# set the start with maximum exposure time
pyautogui.click(x = 1195, y = 65) # press adjust button
num = 22
time.sleep(1)
pyautogui.click(x = 200, y = 204) # press exposure time button ,make exposure time defult 22
time.sleep(2)
pyautogui.tripleClick(x = 200, y = 204, interval = 0.3)
time.sleep(1)
pyautogui.press('backspace', presses= 6)
autoit.send(str(num))
pyautogui.click(x = 210, y = 326) # press apply
time.sleep(5)
cond = 'good'
while True:
    print (str(num))
    im = pyscreeze.screenshot(region=(420,182, 120, 190)) #left, top, width, height
    arr = np.array(im)
    if not search_red(im):
        break
    print (search_red(im))
    print ("found a red pixel") # remove later
    num = num - 1
    if num == 0:
        print ('error in ethernet')
        # pyautogui.click(x = 780, y = 1049)
        # pyautogui.hotkey('alt', 'f4') # close arduino
        cond='red screen'
        send_mail.send_mail(cond)
        time.sleep(2)
        pyautogui.hotkey('alt', 'f4') # close lumo
        autoit.shutdown(2) # restart
        break
    pyautogui.click(x = 200, y = 204) # press exposure time button
    time.sleep(1)
    pyautogui.tripleClick(x = 200, y = 204, interval = 0.3)
    time.sleep(1)
    pyautogui.press('backspace', presses= 6)
    time.sleep(1)
    pyautogui.typewrite(str(num))
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x = 215, y = 323) # press apply
    time.sleep(3)
f.write('line 152')


## record
if cond == 'good':
    pyautogui.click(x = 1305, y = 67) # press capture button
    time.sleep(1)
    pyautogui.click(x = 1181, y = 136) # press record
    time.sleep(1)

#start moving camera farward
move_camera(1)
pyautogui.click(x = 318, y = 750) #press lumo recorder button
table_duration = 350
# time.sleep(table_duration)
countdown(table_duration)

#close lumo recorder
# os.system('taskkill /IM "LumoRecorder-x64.exe" ')
# time.sleep(15)
# try:
#     os.system('taskkill /IM "LumoRecorder-x64.exe" /F')
# finally:
#     pass
# time.sleep(2)

"--------------------------------------------------------------------------------"
f.write('line 179')

#start researchIR, link camera and start recording, bring camera home
pyautogui.click(x= 220, y = 749) # lunch researchIR
time.sleep(1)
pyautogui.hotkey('ctrl', 'l') # connect IR camera
time.sleep(7)
"""make sure FLIR is connecred"""
ir_cond = 'good'
research_IR_img1 = pyscreeze.screenshot()
ir_arr1 = np.array(research_IR_img1)
research_IR_img2 = pyscreeze.screenshot()
ir_arr2 = np.array(research_IR_img2)
while (ir_arr1==ir_arr2).all():
    time.sleep(1)
    pyautogui.click(x= 762, y = 442)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l') # connect IR camera
    time.sleep(7)
    research_IR_img1 = pyscreeze.screenshot()
    ir_arr1 = np.array(research_IR_img1)
    research_IR_img2 = pyscreeze.screenshot()
    ir_arr2 = np.array(research_IR_img2)
f.write('line 202')

time.sleep(1)
pyautogui.click(x= 602, y = 323) # Press middle screen
time.sleep(1)
"""countdown the time it takes to record everything"""
move_camera(2)
pyautogui.click(x= 220, y = 749) # lunch researchIR
time.sleep(1)
pyautogui.hotkey('f5') # record 300 sec
""""""
#start moving camera farward
f.write('line 214')

countdown(320)
# pyautogui.click(x= 220, y = 749) # lunch researchIR
"""
seq file is saved to current_seq
renameit current.seq
open it with researchir
process it to a folder inside current
then rename it to date and time and move to recorded_seq folder
move the tiff to that folder as well under a folder with the same date-time
delete files in current
"""
folder_path = r'C:\Users\Owner\Documents\ResearchIR Data\Current_seq'
f.write('line 228')

#the recorded seq
recorded_seq = glob.glob(os.path.join(folder_path,'*.seq'))
print (recorded_seq)
#rename it to 'current'
os.rename(os.path.join(folder_path,recorded_seq[0]), os.path.join(folder_path,'Current.seq'))

#open current.seq with researchIR
pyautogui.click(x= 15, y = 31) # Press researchIR FILE button
time.sleep(1)
pyautogui.click(x= 37, y = 50) # Press researchIR OPEN button
time.sleep(1)
pyautogui.click(x= 243, y = 440) # Press researchIR to enter the name of the file
time.sleep(1)
autoit.send('Current.seq')
time.sleep(1)
pyautogui.press('enter')  # press the Enter key
time.sleep(10)
pyautogui.click(x= 15, y = 31) # Press researchIR FILE button
time.sleep(1)
pyautogui.click(x= 43, y = 132) # Press researchIR EXPORT button
time.sleep(1)
pyautogui.click(x= 794, y = 614) # Press researchIR EXPORT button in export menu
f.write('line 252')

"""countdown the amount of time it takes to export everything"""
time.sleep(45)
""""""
pyautogui.hotkey('ctrl', 'l') # connect IR camera
f.write('line 258')

#renameit to date-time and move to recorded_seq folder
recorded_path = r'C:\Users\Owner\Documents\ResearchIR Data\Current_seq\Recorded_seq'
now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
os.rename(os.path.join(folder_path,'Current.seq'),os.path.join(recorded_path,now+'.seq'))
#copy the tiffs folder
shutil.copytree(folder_path+'/Tiffs', recorded_path+'/'+now)
#clear the original tiff folder
files = glob.glob(folder_path+'/Tiffs/*')
for g in files:
    os.remove(g)

# pyautogui.hotkey('alt', 'f4') # close arduino

#lunch lumo to keep camera on
# subprocess.call(r'C:\Program Files\Specim\Lumo - Recorder\2018_517\LumoRecorder-x64.exe')
f.write('line 275')

#send e-mail
if len(os.listdir(r'D:\Data')) > num_of_dirs:
    cond='good'
    send_mail.send_mail(cond)
    time.sleep(2)
else:
    cond='bad'
    send_mail.send_mail(cond)
    time.sleep(2)
f.write('line 286')

# print ('the camera will remain on and will shutdown in:')
# countdown(2400)
#time.sleep(2400)
# pyautogui.hotkey('alt', 'f4') # close Lumorecorder
# autoit.shutdown(2)