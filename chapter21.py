#スタックを使用して文字列やリストを逆転させる

# coding: UTF-8
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack1 = Stack()
    for c in "yesterday":
        stack1.push(c)
    reverse = ""
    while stack1.size():
        reverse += stack1.pop()
    print("逆さにすると" + reverse)

    stack2 = Stack()
    list = [1,2,3,4,5]
    reverse_list = []
    for num in list:
        stack2.push(num)
    while stack2.size():
        reverse_list.append(stack2.pop())
    print("逆さにすると" + str(reverse_list))