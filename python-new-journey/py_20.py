# 去掉字符串中不需要的字符

s = '   abc  123  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = '---abc+++'
print(s.strip('-+'))

s = 'abc:123'
print(s[:3] + s[4:])

s = '\tabc\t123\txyz'
print(s.replace('\t',''))

s = '\tabc\t123\txyz\rqix'
import re
print(re.sub('[\t\r]', '', s))

s = 'abc123xyz'
print(s.translate(str.maketrans('abcxyz', 'xyzabc')))