# ProxyHandler处理器\(代理\)

1. 代理的原理:在请求目的服务器之前，先请求代理服务器，然后让代理服务器去请求目的网站，代理服务器拿到目的网站的数据后，在转发给我们的代码
2. [http://httpbin.org](http://httpbin.org) 这个网站可以方便查看http请求的一些参数
3. 在代码中使用代理
   * 使用 `urllib.request.ProxyHandler` 传入一个代理，这个代理是一个字典，字典的key依赖于代理服务器能够接受的类型，一般是 `http` 或者 `https`,值是`ip:port`
   * 使用上一步创建的`handler` 以及 `request.build_opener`创建一个`opener`对象
   * 使用上一步创建的`opener` 调用`open`函数，发起请求
4. 示例代码如下：

   \`\`\`python from urllib import request

url = '[http://www.httpbin.org/ip](http://www.httpbin.org/ip)'

## 1.使用 ProxyHandler 传入代理构建一个handler

handler = request.ProxyHandler\({"http":"58.87.68.189:1080"}\)

## 2.使用 handler 构建一个opener

opener = request.build\_opener\(handler\)

## 3.使用 opener发送一个请求

resp = opener.open\(url\)

print\(resp.read\(\)\) \`\`\`

