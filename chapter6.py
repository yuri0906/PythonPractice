#文字列操作のメソッドを実装

# coding: UTF-8

def fillIntheBlank(word1,word2):
    print("私は昨日、{}を書いて、{}に送った".format(word1,word2))

def upperFirstChar(englishSentence):
    try:
        print(englishSentence.capitalize())
    except:
        print("error!英文を入力してください。")

def splitSentence(sentence,period):
    print(sentence.split(period))

def linkingWords(wordsList):
    print(" ".join(wordsList))

def replaceChar(sentence,character,replace):
    print(sentence.replace(character,replace))

def searchIndex(sentence,character):
    try:
        print(sentence.index(character))
    except:
        print("見つかりませんでした。")

def sliceSentence(sentence,period):
    sliceSentence = sentence.split(period)
    print(sliceSentence[0])


if __name__ == "__main__":
    print("----fillIntheBlank----")
    fillIntheBlank("仕事の用件","Aさん")

    print("----upperFirstChar----")
    upperFirstChar("i like icecream")

    print("----splitSentence----")
    splitSentence("私は||今日||公園に||行った。","||")

    print("----linkingWords----")
    linkingWords(["A","P","P","L","E"])

    print("----replaceChar----")
    replaceChar("てうてう","て","ちょ")

    print("----searchIndex----")
    searchIndex("あいうえお","あ")
    
    print("----sliceSentence----")
    sliceSentence("4月の晴れた寒い日で、時計がどれも13時を打っていた","、")

