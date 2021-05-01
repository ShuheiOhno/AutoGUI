# 最初はこちらで、ボタンの座標を測定する
# 実行した後、ボタンまでマウスを移動させ、ターミナルを確認し、座標を確認してください。座標は、auto.pyで使用します。

import pyautogui
print('中断するには、ctr+c')
try:
    while True:
        x,y = pyautogui.position()
        position_str = 'x: ' + str(x).rjust(4) + 'y: ' + str(y).rjust(4)
        print(position_str,end='')
        print('\b'*len(position_str), end='',flush=True)
except KeyboardInterrupt:
    print('終了')