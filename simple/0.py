# -*- coding: utf-8 -*-

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列

# # 打印1000以内的素数:
# # for n in primes():
# #     print(n)



# def is_palindrome(n):
#     return str(n)==(str(n))[::-1]

# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# list(filter(is_palindrome, range(1, 200)))

