# Eliga Franks
# Project 1
# Reading in the vertices and calculating the perimeter and area.

from Lab3.Point import Point
from Polygon import Polygon
from Rectangle import Rectangle

file = open("Project1.txt", "r")

with open("Project1.txt", "r") as file:
    row = file.readline()
    array = row.split()
    num_vert = int(array[1])
    shapeL = array[0]

    while row != '':

        array = row.split()
        shapeL = array[0]
        num_vert = int(array[1])
        points_list = []

        for i in range(1, num_vert + 1):
            row = file.readline()
            array = row.split()
            point = Point(float(array[0]), float(array[1]))
            points_list.append(point)

        # print(points_list)
        if shapeL == 'P':
            print("")
            print("Vertices for the polygon are\n")
            mypolygon = Polygon(points_list)
            print(mypolygon)
            print("Using Polygon's perimeter routine")
            print(mypolygon.perimeter())
            print("Using Polygon's area routine")
            print(mypolygon.area())


        elif shapeL == 'R':
            print("")
            print("Vertices for the rectangle are\n")
            myrectangle = Rectangle(points_list)
            print(myrectangle)
            print("Using Rectangle's perimeter routine")
            print(myrectangle.perimeter())
            print("Using Rectangle's area routine")
            print(myrectangle.area())

        row = file.readline()
