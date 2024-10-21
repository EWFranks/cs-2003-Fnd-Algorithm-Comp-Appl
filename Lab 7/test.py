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

        if self.rear is None:
            self.front = Node(item)
            self.rear = self.front
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            return None
        else:
            retunreditem = self.front.data
            self.front = self.front.next
            return retunreditem

    def size(self):
        return self.width


def main():
    q = Queue()
    j = q.dequeue()
    print(q.isEmpty())
    print(q.size())

    q.enqueue(136)
    print(q.isEmpty())
    print(q.size())

    q.enqueue(120)
    print(q.isEmpty())
    print(q.size())

    q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    q.enqueue(101)
    q.enqueue(135)
    q.enqueue(105)
    print(q.isEmpty())
    print(q.size())

    q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())

    q.dequeue()
    print("item removed is;", j)
    print(q.isEmpty())
    print(q.size())


main()
