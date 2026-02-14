class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height

class Square(rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.height = height
        self.width = height
def resize_rectangle(rect, new_width, new_height):
    rect.set_width(new_width)
    rect.set_height(new_height)
    return rect.width * rect.height

rect = rectangle(2, 3)
print("Area of rectangle before resize:", resize_rectangle(rect, 4, 5))
Square = Square(4)
print("Area of square before resize:", resize_rectangle(Square, 5, 10))