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


print(Square(5).square_area())
print(Shape().shape_area())
