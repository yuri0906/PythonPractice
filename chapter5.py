# coding: UTF-8

lis = ["a","b","c"]
tup = ("a","b","c") 
dic = {"a":"x","b":"y","c":"z"}

dic2 = {
    "aaa":["あ","い","う","え","お"],
    "bbb":["か","き","く","け","こ"],
    "ccc":["さ","し","す","せ","そ"],
}

def pickUpFromDic(key):
    print(dic[key])

def pickUpFromDic2(key,num):
    print(dic2[key][num])

def main():
    pickUpFromDic("あ")
    pickUpFromDic2("aaa",1)

main()