import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# # 削除ボタンにカーソルを持っていく
# # 削除ボタンをクリック

repeatNumber = 9000
for i in range(repeatNumber):

    pyautogui.click(341,359,duration=1)
    # pyautogui.click(1100,1100,duration=1)

    # #2秒後はいを押す
    time.sleep(2)
    # pyautogui.click(1256,932,duration=1)
    # pyautogui.moveTo(341,359,duration=1)
    pyautogui.keyDown('enter')

    # pyautogui.moveTo(341,365,duration=4)
    # pyautogui.moveTo(341,359,duration=3)
# #     # # 5秒まつ
    time.sleep(3)



#mause
# print('中断するには、ctr+c')
# try:
#     while True:
#         x,y = pyautogui.position()
#         position_str = 'x: ' + str(x).rjust(4) + 'y: ' + str(y).rjust(4)
#         print(position_str,end='')
#         print('\b'*len(position_str), end='',flush=True)
# except KeyboardInterrupt:
#     print('終了')
