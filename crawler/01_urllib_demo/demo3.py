from urllib import request, parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# resp = request.urlopen(url)
# print(resp.read())

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'

headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))