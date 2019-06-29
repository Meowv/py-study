from random import randint

# 多滤掉列表中的负数
data = [randint(-10, 10) for _ in range(10)]

print(data)

result_1 = filter(lambda x: x >= 0, data)
result_2 = [x for x in data if x >= 0]

print(list(result_1))
print(list(result_2))