# coding: UTF-8

def mul_four(num):
    print(num*4)

def div_two(num):
    print(num/2)

def convert_float(num):
    try:
        print(float(num))
    except:
        print("不正な値です")

def main():
    num = input("数字を入力してください:")
    convert_float(num)

main()