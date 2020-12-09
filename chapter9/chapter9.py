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
        

def main():
    data = [
        ["あ","い","う","え","お"],
        ["あ","い","う","え","お"],
        ["あ","い","う","え","お"]
    ]
    addCSV(data)

main()