# 将多个小字符串拼接成一个大字符串

s1 = 'abcdefg'
s2 = '12345'

print(s1 + s2)
print(str.__add__(s1, s2))

pl = ["<0112>", "<32>", "<1024x168>", "<60>", "<1>", "<100.0>", "<500.0>"]

s = ''

for p in pl:
    s += p
    print(s)

print(s)

print(''.join(['abc', '123', 'xyz']))

print(''.join(pl))

l  = ['abc', 123, 45, 'xyz']

print(''.join(str(x) for x in pl))