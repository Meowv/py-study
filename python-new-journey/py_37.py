# 通过实例方法名字的字符串调用方法

from lib1 import Circle
from lib2 import Rectangle
from lib3 import Triangle

def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()

shape1 = Circle(2)
shape2 = Triangle(3,4,5)
shape3 = Rectangle(6,4)

shapes = [shape1,shape2,shape3]

print(list(map(getArea,shapes)))


from operator import methodcaller

s = 'abc123abc456'
print(s.find('abc', 4))
print(methodcaller('find', 'abc', 4)(s))