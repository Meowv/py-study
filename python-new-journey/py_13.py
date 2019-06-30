# 对迭代器做切片操作

from itertools import islice

f = open('python-new-journey/LICENSE', 'r').readlines()

for line in islice(f ,10, 20):
    print(line)

l = range(20)

t = iter(l)

for x in islice(t, 5 , 10):
    print(x)

for x in t:
    print(x)