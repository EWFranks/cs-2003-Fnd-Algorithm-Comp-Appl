class HashTable:  # hashingDAS2.py    closed hashing = open addressing
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        print("For key: ", key, ", trying index ", hashvalue, "with data: ", data);


        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                i = 1
                nextslot = self.rehash(hashvalue, len(self.slots), i)
                print("For key: ", key, ",    now trying index ", nextslot, "with data: ", data)

                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] != key:
                    i = i + 1
                    nextslot = self.rehash(nextslot, len(self.slots), i)

                    print("For key: ", key, ",    now trying index ", nextslot, "with data: ", data)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        key = key * key
        key = str(key)
        return int(key[len(key) - 2] + key[len(key) - 1]) % size

    def rehash(self, oldhash, size, i):

        return oldhash + (i * i) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        i = 1
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots), i)
                if position == startslot:
                    stop = True
                i = i + 1
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[52] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print()
print("The slots:")
print(H.slots)
print("The data:")
print(H.data)

print(H[20])

print(H[17])
H[20] = 'duck'

print()
print("The slots:")
print(H.slots)
print("The data:")
print(H.data)

print(H[20])
print(H[99])

