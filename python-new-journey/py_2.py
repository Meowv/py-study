from random import randint

# 筛出字典中值高于90的项
d = {x: randint(60, 100) for x in range(1, 21)}

print(d)

result = {k: v for k, v in d.items() if v > 90 }

print(result)