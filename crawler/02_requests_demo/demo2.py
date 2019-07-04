import requests

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}

headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchlloJob=0', data=data, headers=headers)

print(response.text)
print(response.json())