# Eliga Franks
# Lab 3
# Reading in the number of verttices

file = open("../Lab3/Project1.txt", "r")

with open("../Lab3/Project1.txt", "r") as file:
    row = file.readline()
    array = row.split()
    lines1_to_read = [1, 2, 3, 4, 5]
    lines2_to_read = [6, 7, 8, 9, 10]
    lines3_to_read = [12, 13, 14, 15]
    lines4_to_read = [17, 18, 19]

    norCount = 0

    while row == '':

        if array[0] == 'P':
            print("Reading vertices for a polygon with 5 vertices\n")

        elif array[0] == 'R':
            print("Reading vertices for a rectangle having 4 vertices\n")

        else:
            norCount + 1
            print("Vertex", norCount, "has coordinates at\n")
            print("{:1.2f}".format(float(array[0])), "{:1.2f}".format(float(array[1], "\n")))

            row = file.readline()
