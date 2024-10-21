from Polygon import Polygon

class Rectangle(Polygon):
    def __init__(self):
        super().__init__()
        self.length=6.0
        self.width=4.0

    def perimeter(self):
        print ("Using Rectangle's perimeter routine")
        return 2*self.length+2*self.width


