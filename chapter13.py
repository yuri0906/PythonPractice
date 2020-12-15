#継承、コンポジションを使用したクラスの実装

# coding: UTF-8

class Shape:
    def what_am_i(self):
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

class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider 
class Rider:
    def __init__(self,name):
        self.name = name

if __name__ == "__main__":
    print("----継承を使用----")
    rectangle = Rectangle(4,3)
    print(rectangle.caliculate_perimeter())
    rectangle.what_am_i()
    
    print("----コンポジションを使用----")
    mick = Rider("mick")
    star = Horse("star",mick)
    print(star.rider.name)
