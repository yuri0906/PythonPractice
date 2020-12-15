#ループを使ったメソッド実装

# coding: UTF-8

#正解の値を入力するまで無限ループ
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

#同じ添字の値の積で新しいリストを作る
def multiple2D(list1,list2):
    resultList = []
    for i in range(len(list1)):
        resultList.append(list1[i] * list2[i])
    print(resultList)

if __name__ == "__main__":
    print("----infiniteLoop----")
    infiniteLoop()
    print("----multiple2D----")
    multiple2D([1,2],[2,1])

