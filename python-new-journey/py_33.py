# 创建可管理的对象属性

from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRedius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int ,long, float)):
            raise ValueError('wrong type.')
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi

    R = property(getRedius, setRadius)

c = Circle(3.2)
print(c.R)