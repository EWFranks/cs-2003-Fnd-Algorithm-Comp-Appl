# Eliga Franks
# 3-17-21
# OrderedList implementation in accord to the Day13 posting
import gc


class Node:  # OrderedlistDAS.py
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None


class DoubleLinkedOrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    ###
    def add(self, item):
        nodePos = Node(item)
        nodePos.next = None
        nodePos.prev = None

        if self.isEmpty():
            self.head = nodePos
            return
        tempPosition = self.head
        while tempPosition is not None:
            if item <= tempPosition.data:
                if tempPosition == self.head:
                    self.head.prev = nodePos
                    nodePos.next = self.head
                    self.head = nodePos
                    return
                nodePos.prev = tempPosition.prev
                nodePos.next = tempPosition
                tempPosition.prev.next = nodePos
                tempPosition.prev = nodePos
                return
            if tempPosition.next is None:
                nodePos.prev = tempPosition
                tempPosition.next = nodePos
                return
            tempPosition = tempPosition.next

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next

        return found

    def remove(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                if self.head == current:
                    if self.head.next is None:
                        self.head = None
                        return
                    self.head.next.prev = None
                    self.head = self.head.next
                    return
                if current.next is None:
                    current.prev.next = None
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

    def __str__(self):
        returnString = "The ordered list contents: "
        current = self.head
        while current is not None:
            returnString = (returnString + " " + str(current.data))
            current = current.next
        return returnString

    def pop(self, pos):
        if self.head is None:
            return None
        if pos == 0 and self.head.next is None:
            item = self.head.data
            self.head = None
            return item
        if pos == 0:
            item = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
            return item
        current = self.head
        iterate = 0
        while current is not None:
            if iterate == pos:
                if current.next is None:
                    item = current.data
                    current.prev.next = current.next

                    return item
                item = current.data
                current.prev.next = current.next
                current.next.prev = current.prev
                return item
            iterate += 1
            current = current.next
        return None


mylist = DoubleLinkedOrderedList()
print(mylist)
print("...adding 31")
mylist.add(31)
print(mylist)
print("...adding 77")
mylist.add(77)
print(mylist)
print("...adding 17")
mylist.add(17)
print(mylist)
print("...adding 93")
mylist.add(93)
print(mylist)
print("...adding 26")
mylist.add(26)
print(mylist)
print("...adding 54")
mylist.add(54)
print(mylist)
print("length is: ", mylist.length())
print("search for 93 successful: ", mylist.search(93))
print("search for 100 successful:", mylist.search(100))
print("...adding 100")
mylist.add(100)
print(mylist)
print("search for 100 successfull: ", mylist.search(100))
print("length is: ", mylist.length())
print("...removing 54...")
mylist.remove(54)
print(mylist)
print("length is: ", mylist.length())
print("...removing 93")
mylist.remove(93)
print(mylist)
print("length is: ", mylist.length())
print("...removing 31")
mylist.remove(31)
print(mylist)
print("length is: ", mylist.length())
print("search for 93 successful: ", mylist.search(93))
print(mylist.pop(2))
print(mylist)
print(mylist.pop(0))
print(mylist)
