# 让类支持比较操作

from functools import total_ordering
from abc import ABCMeta, abstractmethod



@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()

    def __eq__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() == obj.area()

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14
    
r1 = Rectangle(5,3)
r2 = Rectangle(4,4)

c1 = Circle(3)

print(r1 < r2)
print(r1 <= r2)

print(r1 <= c1)
print(c1 > r1)
print(c1 == 1)