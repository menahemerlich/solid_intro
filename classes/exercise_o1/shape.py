
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
        self.area1 = (radius ** 2) * 3.14
        return self.area1

class Square(Shape):
    def area(self, square):
        self.area2 = square ** 2
        return self.area2

class Rectangle(Shape):
    def area(self, length, width):
        self.area3 = length * width
        return self.area3


