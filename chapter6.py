# coding: UTF-8

def eachPrintString(input):
    for char in input:
        print(char)

def fillIntheBlank(word1,word2):
    print("私は昨日、{}を書いて、{}に送った".format(word1,word2))

def upperFirstChar(englishSentence):
    try:
        print(englishSentence.capitalize())
    except:
        print("英文を入力してください")

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
        print("Not Found")

def sliceSentence(sentence,period):
    sliceSentence = sentence.split(period)
    print(sliceSentence[0])

def main():
    sliceSentence("4月の晴れた寒い日で、時計がどれも13時を打っていた","、")

main()