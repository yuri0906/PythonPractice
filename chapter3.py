#入力した数字で、年齢の条件分岐を行う

# coding: UTF-8

def showAge(age):
    try:
        age = int(age)
        if age <= 10:
            print("あなたは10歳以下です。")
        elif age > 10 and age <= 25:
            print("あなたは10~25歳です。")
        else:
            print("あなたは25歳以上です。")
    except:
        print("不正な値です。")

if __name__ == "__main__":
    age = input("年齢を入力してください：")
    showAge(age)



