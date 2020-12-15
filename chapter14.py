# coding: UTF-8

class Square:
    squares = []

    def __init__(self,length):
        self.length = length
        self.squares.append((self.length))
    
    def caliculate_perimeter(self):
        return self.length*self.length
