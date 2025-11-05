from classes .exercise_o1.shape import Shape

class Rectangle(Shape):
    def area(self, length, width):
        self.area3 = length * width
        return self.area3