class Shape():
    def _init_(self):
        pass
    def shape_area(self):
        return 0

class Square(Shape):
    def _init_(self, length):
        self.length = length
    def square_area(self):
        return self.length * self.length

class Rectangle(Shape):
    def _init_(self, length, width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        return self.length * self.width


print(Square(5).square_area())
print(Shape().shape_area())
print(Rectangle(5,2).rectangle_area())


