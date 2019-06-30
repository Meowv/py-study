# 让字典保持有序

# d = {}
# d['Jim'] = (1,35)
# d['Leo'] = (2,37)
# d['Bob'] = (3,40)

# for k in d: print(k)

# from collections import OrderedDict

# d = OrderedDict()
# d['Jim'] = (1,35)
# d['Leo'] = (2,37)
# d['Bob'] = (3,40)

# for k in d: print(k)

from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in range(8):
    input()
    p = players.pop(randint(0, 7-i))
    end = time()
    print(i + 1, p , end-start)
    d[p] = (i+1,end-start)

for k in d:
    print(k, d[k])