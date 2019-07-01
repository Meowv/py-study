# 判断字符串a是否以字符串b开头或结尾

import os, stat

files = os.listdir('python-new-journey/files')

print(files)

# s = 'g.sh'
# print(s.endswith('.sh'))
# print(s.endswith('.py'))

result = [name for name in files if name.endswith(('.sh','.py'))]

print(result)