import math
class Point:

    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y

    def __str__(self):
#       return(str(self.x) + "  " + str(self.y))
        return ("{:.2f}".format(self.x) + "  " + "{:.2f}".format(self.y))

    def translate(self,a=0.0,b=0.0):
        self.x=self.x+a
        self.y=self.y+b

    def scale(self,sx=0.0,sy=0.0):
        self.x=self.x*sx
        self.y=self.y*sy

    def rotate(self, theta_in_degrees=0.0):
        theta = (2.0 * 3.14159 / 360.0)*theta_in_degrees
        old_x=self.x
        old_y=self.y
        self.x = (old_x*math.cos(theta)+old_y*math.sin(theta))
        self.y = (-old_x*math.sin(theta)+old_y*math.cos(theta))

    def distance(self, otherpoint):

        a = self.x - otherpoint.x
        b = self.y - otherpoint.y
        return math.sqrt(a ** 2 + b ** 2)



