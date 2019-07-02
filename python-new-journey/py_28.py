# 解析/构建 XML文档

# from xml.etree.ElementTree import parse

# f = open('demo.xml')

# et = parse(f)

# root = et.getroot()

# for child in root:
#     print(child.get('item'))

# list(root.iter())

# ....

from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import tostring

e = Element('Data')
print(e.tag)

e.set('name', 'abc')
print(tostring(e))

e2 = Element('Row')

e3 = Element("Open")
e3.text = '8.80'

e2.append(e3)

print(tostring(e2))

e.text = None

e.append(e2)

print(tostring(e))

et = ElementTree(e)

et.write('demo.xml')