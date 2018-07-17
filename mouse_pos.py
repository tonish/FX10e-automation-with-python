import pyautogui
import autoit
import sys

print 'Press Ctrl-C to quit.'
try:
    while True:
         x, y = pyautogui.position()
         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
         pyautogui.alert(positionStr)
#         print '\b' * len(positionStr)
except KeyboardInterrupt:
    print '\n'

# # for i in pyautogui.locateAllOnScreen('looksLikeThis.png'):
# #     print i