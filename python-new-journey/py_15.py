# 拆分含有多种分隔符的字符串

import re

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

# def mySplit(s, ds):
#     res = [s]

#     for d in ds:
#         t = []
#         map(lambda x: t.extend(x.split(d)), res)
#         res = t
#     return [x for x in res if x]

# print(mySplit(s,';,|\t'))

print(re.split(r'[;,|\t]+', s))