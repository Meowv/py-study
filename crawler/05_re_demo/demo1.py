import re

# 匹配某个字符串
text = 'hello'
ret = re.match('he', text)
print(ret.group())

# 点(.)匹配任意字符
text = 'hello'
ret = re.match('.',text)
print(ret.group())

# \d 匹配任意的数字(0-9)
text = '1'
ret = re.match('\d',text)
print(ret.group())

# \D 匹配任意非数字
text = 'a1'
ret = re.match('\D',text)
print(ret.group())

# \s 匹配空白字符(\n,\t,\r,空格)
text = '\t'
ret = re.match('\s', text)
print(ret.group())

# \w 匹配 a-z、A-Z、数字、下划线
text = '_'
ret = re.match('\w', text)
print(ret.group())

# \W 匹配与\w 相反
text = '+'
ret = re.match('\W', text)
print(ret.group())

# 组合的方法，只要满足中括号中的字符，就可以匹配
text = 'a'
ret = re.match('[a1]', text)
print(ret.group())

text = '021-88888888abcd'
ret = re.match('[\d\-]+', text)
print(ret.group())

# 中括号的形式代替 \d
text = '09'
ret = re.match('[0-9]', text)
print(ret.group())

# 中括号的形式代替 \D
text = 'A'
ret = re.match('[^0-9]', text)
print(ret.group())

# 中括号的形式代替 \w
text = '_'
ret = re.match('[a-zA-Z0-9_]', text)
print(ret.group())

# 中括号的形式代替 \W
text = '+'
ret = re.match('[^a-zA-Z0-9_]', text)
print(ret.group())