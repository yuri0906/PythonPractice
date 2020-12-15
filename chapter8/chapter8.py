#他のモジュールをインポートする

# coding: UTF-8

import cubed

if __name__ == "__main__":
    num = input("数字を入力してください：")
    try:
        print(cubed.cubed(int(num)))
    except:
        print("不正な値です。")
