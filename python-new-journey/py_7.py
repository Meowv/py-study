# 快速找到多个字典中的公共键

from random import randint, sample

s1 =  {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1)

s2 =  {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s2)

s3 =  {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s3)

res = []

for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print(res)

# viewkeys
# map
# reduce