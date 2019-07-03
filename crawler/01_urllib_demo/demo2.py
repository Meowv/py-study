from urllib import parse

# urlparse and urlsplit
# 用法基本一致,urlparse有params属性,urlsplit没有

url = 'http://www.baidu.com/s?wd=python&username=qix#1'

result1 = parse.urlparse(url)
print(result1)
print('scheme:', result1.scheme)
print('netloc:', result1.netloc)
print('path:', result1.path)
print('params:', result1.params)
print('query:', result1.query)
print('fragment:', result1.fragment)

result2 = parse.urlsplit(url)
print(result2)
print('scheme:', result2.scheme)
print('netloc:', result2.netloc)
print('path:', result2.path)
print('query:', result2.query)
print('fragment:', result2.fragment)