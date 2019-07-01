# 对字符串进行左、右、居中对齐

s = 'abc'

print(s.ljust(20))
print(s.ljust(20, '='))

print(s.rjust(20))
print(len(s.rjust(20)))

print(s.center(20))

print(format(s, '<20'))
print(format(s, '>20'))
print(format(s, '^20'))

d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}

print(d.keys())

w = max(map(len, d.keys()))
print(w)

for k in d:
    print(k.ljust(w), ':', d[k])