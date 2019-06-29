# 根据字典中值的大小，对字典中的项排序

from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
print(d)

print(sorted(d))

print(list(iter(d)))

z = list(zip(d.keys(), d.values()))

print(z)

result = sorted(z)
print(result)

result = sorted(d.items(), key=lambda x: x[1])

print(result)