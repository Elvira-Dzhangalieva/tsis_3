
import math

class Point():
    def _init_(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def dist(self, ch):
        X = ch.x - self.x
        Y = ch.y - self.y
        return math.sqrt((X*2)+(Y*2))
p1 = Point(1, 2)
print(p1.show())

p2 = Point(3, 4)
print(p2.show())

p1.move(4, 6)
print(p1.show())

p2.move(6, 4)
print(p2.show())

print(p1.dist(p2))
