# 反向迭代以及实现反向迭代

# l = [1,2,3,4,5]
# print(l[::-1])

# for x in reversed(l):
#     print(x)

class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >- self.start:
            yield t
            t -= self.step

for x in FloatRange(1.0, 4.0, 0.5):
    print(x)

for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)