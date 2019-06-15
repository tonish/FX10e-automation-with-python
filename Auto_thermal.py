import autoit
import pyautogui
import send_mail_9_5_2018 as send_mail
import time
import datetime
import os
import pyscreeze
import PIL.ImageGrab as imagegrab
import numpy as np
import shutil
import glob
#import ethernet_state


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
    pyautogui.click(x=1186, y=63)  # press adjust button
    im1 = imagegrab.grab()
    time.sleep(2)
    im2 = imagegrab.grab()
    if im1 == im2:
        return False
    else:
        return True

#logger file
f = open(r"C:\Users\Owner\Documents\ResearchIR Data\logger.txt", "w+")


send_mail.send_mail('start')
time.sleep(2)
f.write('line 78')

num_of_dirs = len(os.listdir(r'C:\Users\Owner\Documents\ResearchIR Data\Current_seq\Recorded_seq'))

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
    pyautogui.click(x= 762, y = 442)
    pyautogui.hotkey('ctrl', 'l') # connect IR camera
    time.sleep(7)
    research_IR_img1 = pyscreeze.screenshot()
    ir_arr1 = np.array(research_IR_img1)
    research_IR_img2 = pyscreeze.screenshot()
    ir_arr2 = np.array(research_IR_img2)
f.write('line 101')

time.sleep(1)
pyautogui.click(x= 602, y = 323) # Press middle screen
time.sleep(1)
"""countdown the time it takes to record everything"""
move_camera(2)
pyautogui.click(x= 220, y = 749) # lunch researchIR
time.sleep(1)
pyautogui.hotkey('f5') # record 300 sec
""""""
f.write('line 112')


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
f.write('line 127')

#the recorded seq
recorded_seq = glob.glob(os.path.join(folder_path,'*.seq'))
print (recorded_seq)
#rename it to 'current'
os.rename(os.path.join(folder_path,recorded_seq[0]), os.path.join(folder_path,'Current.seq'))
f.write('line 134')

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
time.sleep(2)
pyautogui.click(x= 43, y = 132) # Press researchIR EXPORT button
time.sleep(2)
pyautogui.click(x= 794, y = 614) # Press researchIR EXPORT button in export menu
f.write('line 152')

"""countdown the amount of time it takes to export everything"""
time.sleep(45)
""""""
pyautogui.hotkey('ctrl', 'l') # connect IR camera
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
f.write('line 168')

# pyautogui.hotkey('alt', 'f4') # close arduino
move_camera(2)
f.write('line 172')
f.close()
#send e-mail
if len(os.listdir(r'C:\Users\Owner\Documents\ResearchIR Data\Current_seq\Recorded_seq')) > num_of_dirs:
    cond='good'
    send_mail.send_mail(cond)
    time.sleep(2)
else:
    cond='bad'
    send_mail.send_mail(cond)
    time.sleep(2)
