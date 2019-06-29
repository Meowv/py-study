from random import randint

# 筛出集合中能被3整除的元素
data = [randint(-10, 10) for _ in range(10)]
s = set(data)

print(s)

result = {x for x in s if x % 3 == 0}

print(result)