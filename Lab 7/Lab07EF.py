# Eliga Franks
# 3-17-21
# Singly linked list version of a Queue.

class Node:
    def __init__(self, initdata):
        self.data = initdata  # The data held within the current Node
        self.next = None  # The next Node object (NOT the data)


class Queue:

    def __init__(self):
        self.front = None  # The front Node object
        self.rear = None  # The rear Node object
        self.width = 0

    def isEmpty(self):
        return self.width == 0

    def enqueue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = temp  # front number of node taken
            self.rear = self.front
        else:
            self.rear.next = temp  # the next rear is then taken as the value
            self.rear = self.rear.next  # the value is stored in the rear
        self.width = self.width + 1

    def dequeue(self):

        if self.front is None:
            return None
        elif self.front == self.rear:
            self.rear = None
            self.front = None
            self.width = self.width - 1
        else:
            temp = self.front  # front value
            self.front = temp.next  # next part will move to the front
            self.width = self.width - 1
            return temp.data

    def size(self):
        return self.width


def main():
    q = Queue()
    print(q.isEmpty())
    print(q.size())

    q.enqueue(136)
    print(q.isEmpty())
    print(q.size())

    q.enqueue(120)
    print(q.isEmpty())
    print(q.size())

    j = q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    j = q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    q.enqueue(101)
    q.enqueue(135)
    q.enqueue(105)
    print(q.isEmpty())
    print(q.size())

    j = q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    j = q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    j = q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())


main()
