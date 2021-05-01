# 最初に、クリックするボタンの座標を、position.pyを実行して測定してください。

import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# クリックを繰り返す回数
repeatNumber = 9000
for i in range(repeatNumber):

    # position.pyで測定した、ボタンの座標を入力してください。
    pyautogui.click(x=341,y=359,duration=1)

    # 2秒後ボタンを押す
    time.sleep(2)

    # エンターキーを押します。
    pyautogui.keyDown('enter')

    # 3秒待った後、ボタンをクリックします。
    time.sleep(3)

