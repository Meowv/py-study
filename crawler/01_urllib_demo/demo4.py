from urllib import request

url = 'http://www.httpbin.org/ip'

# 无代理
resp = request.urlopen(url)
print(resp.read())

# 使用代理
# 1.使用 ProxyHandler 传入代理构建一个handler
# 2.使用 handler 构建一个opener
# 3.使用 opener发送一个请求
handler = request.ProxyHandler({"http":"58.87.68.189:1080"})
opener = request.build_opener(handler)
resp =  opener.open(url)
print(resp.read())