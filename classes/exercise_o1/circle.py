from classes .exercise_o1.shape import Shape

class Circle(Shape):
    def area(self, radius):
        self.area1 = (radius ** 2) * 3.14
        return self.area1