#数字を入力値として受け取り、簡単な計算をして返す

# coding: UTF-8

def mul_four(num):
    return num * 4

def div_two(num):
    return num / 2

def convert_float(num):
    return float(num)


if __name__ == "__main__":
    num = input("数字を入力してください：")
    try:
        num = int(num)
        print("4をかけたら" + str(mul_four(num)) + "です。")
        print("2で割ると" + str(div_two(num)) + "です。")
        print("floatに変換すると" + str(convert_float(num)) + "です。")
    except:
        print("不正な入力値です。")
