from urllib import request
from urllib import parse

# urlopen
resp = request.urlopen('http://www.baidu.com')

# print(resp.read())
# print(resp.read(100))
# print(resp.readline())
# print(resp.readlines())
# print(resp.getcode())

# urlretrieve
# request.urlretrieve('http://www.baidu.com', 'baidu.html')
# request.urlretrieve('https://s2.ax1x.com/2019/06/23/ZiR4EV.png', 'ms.png')

# urlencode
params = {'name': '张三', 'age' :18, 'greet': 'hello python'}
result =  parse.urlencode(params)

print(result)

url = 'http://www.baidu.com/s'
params = {'wd':'阿星Plus'}
qs = parse.urlencode(params)
url = url + '?' + qs
print(url)
resp = request.urlopen(url)
print(resp.read())

# parse_qs
params = {'name': '张三', 'age' :18, 'greet': 'hello python'}
qs = parse.urlencode(params)
print(qs)
result = parse.parse_qs(qs)
print(result)