from MillerOriginalTextbookCode.Chapter6.binheap import BinHeap
from pythonds.basic import queue
from pythonds.basic.stack import Stack  # Project04.py


class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        self.parent = None  # DAS

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            self.leftChild.parent = self  # DAS
        else:
            t = BinaryTree(newNode)
            t.parent = self  # DAS
            t.leftChild = self.leftChild
            self.leftChild.parent = t  # DAS
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
            self.rightChild.parent = self
        else:
            t = BinaryTree(newNode)
            t.parent = self  # DAS
            t.right = self.rightChild
            self.rightChild.parent = t  # DAS
            self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getParent(self):  # DAS
        return self.parent  # DAS

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# This implementation of a priority queue is essentially
# the  previous binary heap code where, instead of just a key,
# we have (key, value) pairs in the  priority queue.
# It is still just the key, however, that indicates priority.
# We assume that the keys are all comparable  DAS

class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 > self.currentSize:
            return -1
        else:
            if i * 2 + 1 > self.currentSize:
                return i * 2
            else:
                if self.heapArray[i * 2][0] < self.heapArray[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                tmp = self.heapArray[i // 2]
                self.heapArray[i // 2] = self.heapArray[i]
                self.heapArray[i] = tmp
            i = i // 2

    def add(self, k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retkey = self.heapArray[1][0]
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return (retkey, retval)

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False


def count_letter_frequency(char_list):  # Project04ReadText.py  =  Lab12 solution
    letter_frequency = {}
    for letter in char_list:
        keys = letter_frequency.keys()
        if letter in keys:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1

    return letter_frequency


chars = [' ', 'a', 'b', 'd', 'e', 'f', 'h', 'i', 'k', 'n', 'r', 's', 't', 'u', 'v']
freq = [9, 5, 1, 3, 7, 3, 1, 1, 1, 4, 1, 5, 1, 2, 1, 1]
nodes = []

myheap = BinHeap()
myheap.buildHeap(freq)


def hufftree(frequency):
    proxy = queue.PriorityQueue()
    for value in frequency:
        proxy.put(value)
    while proxy.qsize() > 1:
        left = proxy.get()
        node = BinaryTree(left)
        proxy.put((left[0], node))
    return proxy.get()

    node = hufftre(freq)


def iterate(node, est="", spec={}):

    spec = iterate(node)



def main():
    char_list = [ch for ch in open('Project04Input.txt').read() if ch != '\n']
    print("the document")
    for i in range(len(char_list)):
        print(char_list[i], end="")
    print()
    print()

    print("the list of characters in document")
    print(char_list)

    print()

    print("the letter frequency in document")
    letter_frequency = count_letter_frequency(char_list)
    print(letter_frequency)

    print()

    print("the keys in the leaf nodes")
    print(freq)

    print()

    print("keys while building the tree")
    print()

    print()

    print("now the character codes")
    #for i in sorted(freq):
        #print(freq[i[1]])
    print()

    print()

    print("now the encoded document")
    print()


main()
