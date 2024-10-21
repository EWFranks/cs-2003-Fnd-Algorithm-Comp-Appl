import math
from Point import Point
import itertools


class Polygon(object):
    def __init__(self, points_list):
        self.vertices = points_list

    def translate(self, a=0.0, b=0.0):
        for p in self.vertices:
            p.translate(a, b)
            # or equivalently and better p.translate(a,b)

    def scale(self, sx=0.0, sy=0.0):
        for p in self.vertices:
            p.scale(sx, sy)

    def rotate(self, theta_in_degrees=0.0):
        for p in self.vertices:
            p.rotate(theta_in_degrees)

    def __str__(self):
        s = ""
        for p in self.vertices:
            #           s=s+" "+str(p.x)+" "+str(p.y)+"\n"
            s = s + " " + "{:.2f}".format(p.x) + "  " + "{:.2f}".format(p.y) + "\n"
        return s

    # using itertools.cycle
    def perimeter(self):
        distances = []
        circular_buffer = itertools.cycle(self.vertices)
        previous_point = next(circular_buffer)
        for i in range(len(self.vertices)):
            point = next(circular_buffer)
            d = point.distance(previous_point)
            distances.append(d)
            previous_point = point
        return "{:.2f}".format(sum(distances))

    def area(self):
        num_vert = len(self.vertices)
        area = 0

        for index in range(num_vert):
            after_index = (index + 1) % num_vert
            var1 = self.vertices[index]
            var2 = self.vertices[after_index]

            area += var1.x * var2.y
            area -= (var2.x * var1.y)
        area = 0.5 * abs(area)
        return "{:.2f}".format(area)