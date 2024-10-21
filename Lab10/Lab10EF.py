f = open("Lab10Input.txt")
Line = ""
for line in f:
    print(line)
print()
array = []
for item in line:
    array.append(item)
print(array)
print()
iter = {}
for item in array:
    if item not in iter:
        iter[item] = 1
    else:
        iter[item] += 1
print(iter)
print()

f.close()


