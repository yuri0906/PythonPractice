# coding: UTF-8

def infiniteLoop():
    correctAnswer = ["1","3","5","7","9"]
    while True:
        userInput = input("文字を入力してください：")
        if userInput in correctAnswer:
            print("正解")
            break
        elif userInput == "q":
            print("終了")
            break
        else:
            print("不正解")

def multiple2D(list1,list2):
    resultList = []
    for i in range(len(list1)):
        resultList.append(list1[i] * list2[i])

    print(resultList)

def main():
    infiniteLoop()

main()