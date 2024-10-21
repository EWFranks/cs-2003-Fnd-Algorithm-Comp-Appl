#Eliga Franks
#Lab 3
#Reading in the number of vertices

file = open("Project1.txt", "r")

with open("Project1.txt", "r") as file:
    row = file.readline()

    while row != '':
        array = row.split()

        if array[0] == 'P':
            print("Reading vertices for a polygon with", array[1], "vertices")

        elif array[0] == 'R':
            print("Reading vertices for a rectangle with", array[1], "vertices")

        for i in range(1, int(array[1])+1):
            row = file.readline()
            array = row.split()

            print("Vertex", i, "has coordinates at", array[0], array[1])
i+1
        row = file.readline()
