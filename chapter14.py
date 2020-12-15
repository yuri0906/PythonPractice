#クラス変数、isキーワードの利用

# coding: UTF-8

class Square:
    square_list = [] #クラス変数

    def __init__(self,length):
        self.length = length
        self.square_list.append((self.length))
    
def print_size(obj):
    print("{} by {} by {} by {}".format(obj.length,obj.length,obj.length,obj.length))

#前後のオブジェクトが等しいか判断する
def compareObject(obj1,obj2):
    return (obj1 is obj2)

if __name__ == "__main__":
    s1 = Square(3)
    print_size(s1)

    s2 = Square(6)
    print_size(s2)

    s3 = Square(6)
    print_size(s3)

    s4 = Square(9)
    print_size(s4)

    print(Square.square_list)
    
    print(compareObject(s2,s3))
    print(compareObject(s2,s2))