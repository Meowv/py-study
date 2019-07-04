import requests

proxy = {
    'http':'117.90.252.143:9000'
}

response = requests.get('http://www.httpbin.org/ip', proxies=proxy)
print(response.text)
