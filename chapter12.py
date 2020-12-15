#クラスインスタンスの変数表示、メソッド実行

# coding: UTF-8

import math
class Apple:
    def __init__(self,size,weight,mellow,acidity):
        self.size = size
        self.weight = weight
        self.mellow = mellow
        self.acidity = acidity
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.floor(math.pi * self.radius * self.radius)
class Triangle:
    def __init__(self,bottom,height):
        self.bottom = bottom
        self.height = height

    def area(self):
        return (self.bottom*self.height) / 2
class Hexagon:
    def __init__(self,oneSideLength):
        self.oneSideLength = oneSideLength

    def caliculate_perimeter(self):
        return self.oneSideLength*6

if __name__ == "__main__":
    apple = Apple(1,2,3,4)
    print(apple.acidity)

    circle = Circle(2)
    print(circle.area())

    triangle = Triangle(4,5)
    print(triangle.area())
    
    hexagon = Hexagon(3)
    print(hexagon.caliculate_perimeter())
