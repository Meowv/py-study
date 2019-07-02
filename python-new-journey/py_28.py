# 解析XML文档

from xml.etree.ElementTree import parse

f = open('demo.xml')

et = parse(f)

root = et.getroot()

for child in root:
    print(child.get('item'))

# ....

list(root.iter())