#ファイルの読み込み、書き出しなどを実装

# coding: UTF-8

import os
import csv

def writeFile(input):
    with open("sample.txt","w",encoding="utf-8") as f:
        f.write(input)

def readFile():
    with open("sample.txt","r",encoding="utf-8") as f:
        print(f.read())

def addCSV(list):
    with open("sample.csv","w",newline='') as f:
        w = csv.writer(f,delimiter=",")
        for item in list:
            w.writerow(item)
        

if __name__ == "__main__":
    print("----TXTファイルにデータを書き出す→読み込み----")
    writeFile("あいうえお")
    readFile()
    
    print("----CSVファイルにデータを追加----")
    data = [
        ["あ","い","う","え","お"],
        ["か","き","く","け","こ"],
        ["さ","し","す","せ","そ"]
    ]
    addCSV(data)
