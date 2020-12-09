# coding: UTF-8

class Shape:
    def __init__(self):
        self.what_am_i()
        
    def what_am_i():
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,depth,width):
        self.depth = depth
        self.width = width

    def caliculate_perimeter(self):
        return self.depth*self.width


class Square(Shape):
    def __init__(self,length):
        self.length = length
    
    def caliculate_perimeter(self):
        return self.length*self.length

    def change_size(self,value):
        self.length = self.length - value


class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self,name):
        self.name = name

def main():
    mick = Rider("mick")
    star = Horse("star",mick)
    print(star.rider.name)

main()