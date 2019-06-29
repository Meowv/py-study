from collections import namedtuple

# 为元组中的每个元素命名，提高程序可读性
# 定义一系列常量、使用collections.namedtuple替代内置tuple

Studennt = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Studennt('qix','25','meal','123@meowv.com')

s2 = Studennt(name='meowv',age='18',sex='femeal',email='meowv@meowv.com')

print(s)
print(s2)

print(s.name)
print(s2.name)

print(isinstance(s, tuple))