from random import randint

# 统计序列中元素的出现频度

data = [randint(0, 20) for _ in range(0, 30)]
print(data)

c = dict.fromkeys(data, 0)
print(c)

for x in data:
    c[x] += 1

print(c)

from collections import Counter

c2 = Counter(data)
result = c2.most_common(3)

print(result)

import re

txt = open('python-new-journey/LICENSE', 'r').read()

print(txt)

c3 = Counter(re.split('\W+', txt))

result = c3.most_common(10)
print(result)