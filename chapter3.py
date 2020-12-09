# coding: UTF-8

def showAge(age):
    try:
        if age <= 10:
            print("10歳以下です")
        elif age > 10 and age <= 25:
            print("10~25歳です")
        else:
            print("25歳以上です")
    except:
        print("数字を入力してください")

def main():
    age = input("年齢を入力してください:")
    showAge(age)

main()
