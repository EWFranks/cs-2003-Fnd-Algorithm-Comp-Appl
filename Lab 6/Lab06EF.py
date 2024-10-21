# Eliga Franks
# 3-10-21
# Allows results to be an circular array and implement a double edded queue.
import self


class Deque:  # CircularArrayQueue.py   -

    # The original file of Queue basically was the foundation to remove the front item, add an item to the rear,
    # and a resize function that when called it would double the array to be able to fit more items in the array.

    def __init__(self):
        self.items = [None] * 10
        self.size = 0
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items[self.front]

    def removeFront(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        removedItem = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items) #
        self.size -= 1
        return removedItem

    def removeRear(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        removedItem = self.items[self.rear]
        self.items[self.rear] = None
        self.rear = (self.rear - 1) % len(self.items)
        self.size -= 1
        return removedItem

    def getSize(self):
        return self.size

    def resize(self, cap):
        old = self.items
        self.items = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

    def addFront(self, item):
        if self.size == len(self.items):
            self.resize(2 * len(self.items))
        avail = (self.front - 1) % len(self.items)
        self.items[avail] = item
        self.front = avail
        self.size += 1

    def addRear(self, item):
        if self.size == len(self.items):
            self.resize(2 * len(self.items))
        avail = (self.front + self.size) % len(self.items)
        self.items[avail] = item
        self.rear = avail
        self.size += 1


def main():
    q = Deque()
    print(q.isEmpty())
    q.addFront(100)
    print(q.getSize())
    q.addFront(200)
    q.addFront(500.58)
    print(q.getSize())
    print(q.peek())  # print the front item of the queue
    q.addRear(500)
    q.addRear(600)
    q.addFront(3.14)
    print(q.getSize())
    print(q.peek())  # print the front item of the queue
    q.removeFront()
    print(q.getSize())
    print(q.peek())  # print the front item of the queue
    q.addRear("True")
    q.addRear("False")
    print(q.getSize())
    print(q.isEmpty())
    q.addRear(8.4)
    print(q.removeRear())
    print(q.getSize())
    print(q.peek())  # print the front item of the queue
    q.addRear("C++")
    q.addRear("Python")
    q.addRear("Java")
    print(q.getSize())
    q.addFront("Go")
    q.addFront("C")
    print(q.getSize())
    print(q.removeFront())
    q.removeFront()
    q.removeFront()
    print(q.getSize())


main()
