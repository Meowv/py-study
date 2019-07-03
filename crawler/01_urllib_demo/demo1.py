from urllib import request

resp = request.urlopen('http://www.baidu.com')

print(resp.read())
print(resp.read(100))
print(resp.readline())
print(resp.readlines())
print(resp.getcode())

request.urlretrieve('http://www.baidu.com', 'baidu.html')
request.urlretrieve('https://s2.ax1x.com/2019/06/23/ZiR4EV.png', 'ms.png')
