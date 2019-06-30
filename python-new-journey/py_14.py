# 在一个for循环中迭代多个可迭代对象

from random import randint

from itertools import chain

chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
engligh = [randint(60, 100) for _ in range(40)]

# for  i in range(len(math)):
#     chinese[i] + math[i] + engligh[i]

# zip([1, 2, 3, 4], ('a','b','c','d'))

total = []

for c,m,e in zip(chinese,math,engligh):
    total.append(c + m + e)

print(total)

# for x in chain([1,2,3,4],['a','b','c','d']):
#     print(x)

e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(42)]
e3 = [randint(60, 100) for _ in range(42)]
e4 = [randint(60, 100) for _ in range(39)]

count = 0

for s in chain(e1,e2,e3,e4):
    if s > 90:
        count += 1

print(count)