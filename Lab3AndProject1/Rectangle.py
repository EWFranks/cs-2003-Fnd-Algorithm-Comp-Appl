from Polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, point_list):
        super().__init__(point_list)
        self.length = point_list[0].distance(point_list[1])
        self.width = point_list[1].distance(point_list[2])

        def perimeter(self):
            return (2 * self.length) + (2 * self.width)

        def area(self):
            return self.length * self.width
