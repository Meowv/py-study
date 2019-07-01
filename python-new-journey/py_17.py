# 调整字符串中文本的格式

import re

log = open('python-new-journey/files/log.txt', 'r', encoding='utf-8').read()
print(log)

print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log))