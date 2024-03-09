class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def display(self):
        print(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def is_full(self):
        if len(self.items) == self.size:
            return True
        return False

    def push(self, item):
        if not self.is_full():
            self.items += [item]
            self.display()
        else:
            print("데이터를 넣을 저장공간이 부족합니다.")

    def pop(self):
        if not self.is_empty():
            del self.items[-1]
            self.display()
        else:
            print("삭제할 데이터가 없습니다.")

    def peek(self):
        return self.items[-1]


my_stack = Stack(5)

my_stack.display()
print(my_stack.is_empty())
my_stack.pop()
my_stack.push(1)
print(my_stack.is_empty())
print(my_stack.is_full())
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.is_full())
my_stack.push(6)
my_stack.display()
my_stack.pop()
print(my_stack.peek())
