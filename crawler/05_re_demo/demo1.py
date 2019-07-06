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

# * 可以匹配0或者任意个字符
text = '58420abcd'
ret = re.match('\d*', text)
print(ret.group())

# + 可以匹配1或者多个字符
text = 'abcd'
ret = re.match('\w+', text)
print(ret.group())

# ? 可以匹配一个或者0个(要么没有，要么就只有一个)
text = 'abcd'
ret = re.match('\w?', text)
print(ret.group())

# {m} 可以匹配m个字符
text = 'abcd'
ret = re.match('\w{2}', text)
print(ret.group())

# {m,n} 匹配m到n个字符
text = 'abcd'
ret = re.match('\w{1,4}', text)
print(ret.group())

# 匹配手机号码
text = '13477996888'
ret = re.match('1[345789]\d{9}', text)
print(ret.group())

# 验证邮箱
text = 'qix_123@meowv.com'
ret = re.match('\w+@[a-z0-9]+\.[a-z]+', text)
print(ret.group())

# 验证URL
text = 'https://meowv.com'
ret = re.match('(http|https|ftp)://[^\s]+', text)
print(ret.group())

# 验证身份证
text = '40000000000000000X'
ret = re.match('\d{17}[\dxX]', text)
print(ret.group())

# ^
text = 'hello'
ret = re.search('^h', text)
print(ret.group())

# $ 以……结尾
text = '123@meowv.com'
ret = re.match('\w+@meowv.com$', text)
print(ret.group())

# | 匹配多个表达式或者字符
text = 'https'
ret = re.match('(https|http|ftp)$', text)
print(ret.group())

# 贪婪模式和非贪婪模式
text = '0123456'
ret = re.match('\d+?', text)
print(ret.group())

ret = re.match('\d+', text)
print(ret.group())

text = '<h1>title</h1>'
ret = re.match('<.+?>', text)
print(ret.group())

# 匹配0-100之间的数字
text = '99'
ret = re.match('[1-9]\d?$|100$', text)
print(ret.group())