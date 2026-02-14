from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def resize(self, new_width, new_height):
        pass
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def resize(self, new_width, new_height):
        self.side = new_width  # Assume square, so width = height
    def area(self):
        return self.side * self.side
def resize(shape, new_width, new_height):
    shape.resize(new_width, new_height)
    return shape.area()
rect = Rectangle(2, 3)
print("Area of rectangle before resize:", rect.area())
square = Square(4)
print("Area of square before resize:", square.area())

        