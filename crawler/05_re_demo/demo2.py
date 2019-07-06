import re

text = 'apple price is $299'
ret = re.search('\$\d+', text)
print(ret.group())

text = '\\n'
print(text)

text = r'\n'
print(text)

text = '\\a'
ret = re.match('\\\\a', text)
print(ret.group())
