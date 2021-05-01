# AutoGUI
指定したボタンを、任意の時間おきにクリックするプログラム
pythonのバージョン 3.8.5
PyAutoGUIのリンク
https://pyautogui.readthedocs.io/en/latest/index.html
手順
1 AUTOGUIをgit cloneするか、zipファイルをダウンロードする

2 AUTOGUIに移動し、puautoguiをインストールする
ターミナル上でAUTOGUIフォルダに移動し、 pip install pyautogui

3 position.pyを実行し、ボタンの座標を確認する
ターミナル上で python position.py

3 auto.pyを編集する。座標、繰り返したい回数を書き込む。

4 auto.pyを実行する
ターミナル上で、python auto.py

5 途中で中断したい場合は、ターミナル上でCtr+c