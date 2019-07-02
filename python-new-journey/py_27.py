# 读写json数据

import json

l = [1,2,'abc',{'name':'qix','age':18}]

print(json.dumps(l))

d = {'b':None, 'a':5, 'c': 'abc'}

print(json.dumps(d))

print(json.dumps(l,separators=[',',':']))

print(json.dumps(d, sort_keys=True))

l2 = json.loads('[1,2,"abc",{"name":"qix","age":18}]')

print(l2)
print(l2[0])

l2 = json.loads('{"a": 5, "b": null, "c": "abc"}')

print(l2)
print(l2['a'])

with open('demo.json', 'wb') as f:
    json.dump(l, f)