class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def getArea(self):
        a,b,c = self.a,self.b,self.c
        p = (a+b+c) / 2
        area = (p *(p-1) * (p-b) * (p-c)) ** 0.5
        return area