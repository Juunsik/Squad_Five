class Queue:
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

    def add_q(self, item):
        if not self.is_full():
            self.items += [item]
            self.display()
        else:
            print("Queue is full")

    def delete_q(self):
        if not self.is_empty():
            for i in range(len(self.items) - 1):
                self.items[i] = self.items[i + 1]
            del self.items[-1]
            self.display()
        else:
            print("Queue is empty")


my_queue = Queue(5)

my_queue.display()
print(my_queue.is_empty())
my_queue.delete_q()
my_queue.add_q(1)
print(my_queue.is_empty())
print(my_queue.is_full())
my_queue.add_q(2)
my_queue.add_q(3)
my_queue.add_q(4)
my_queue.add_q(5)
print(my_queue.is_full())
my_queue.add_q(6)
my_queue.display()
my_queue.delete_q()
my_queue.add_q(1)
