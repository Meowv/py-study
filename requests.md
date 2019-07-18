# requests

## 发送get请求

发送get请求，直接调用`requests.get`就可以了，想要发送什么类型的请求，就调用什么方法

```python
response = requests.get('https://www.baidu.com/')
```

## response的一些属性

```python
params = {
    'wd': '阿星Plus'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

response = requests.get('https://www.baidu.com/s', params=params, headers=headers)

with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(type(response.text))
print(response.text)

print(type(response.content))
print(response.content.decode('utf-8'))

print(response.url)
print(response.encoding)
print(response.status_code)
```

## response.text和response.content的区别

* response.content 这个是直接从网络上抓取的数据，没有经过任何解码，所以是一个bytes类型。其实在硬盘上和网络上的传输字符串都是bytes类型
* response.text 这个是str的数据类型，是requests库将response.conten进行解码的字符串。解码需要指定一个编码方式。requests会根据自己的猜测来判断编码的方式，所以有时候惠猜测锁雾，就会导致解码产生乱码，这还是就应该使用`response.content.decode('utf-8')`进行手动解码

## 发送post请求

* 发送post请求，直接调用`requests.post`方法就可以了
* 如果返回的是json数据，可以调用`response.json()`来将json字符串转换为字典或者列表

## 使用代理

在请求方法中，传递`proxies`参数就可以了

## 使用cookie

如果想要在多次请求中共享cookie，那么应该使用session，示例代码如下

```python
import requests

url = 'http://www.renren.com/PLogin.do'
data = {
        'email': '13477996338',
        'password': 'Hackxing58420...'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

session = requests.Session()

session.post(url, data=data, headers=headers)

response = session.get('http://www.renren.com/880151247/profile')

with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
```

