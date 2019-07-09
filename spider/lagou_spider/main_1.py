import requests
from lxml import etree
import time

def request_list_page():
    page_url = 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    headers = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'first': 'false',
        'pn': 1,
        'kd': 'python'
    }

    session = requests.Session()
    session.get(page_url, headers=headers)
    cookie = session.cookies

    for x in range(1, 10):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data, cookies=cookie)
        print(response.json())
        time.sleep(1)

def main():
    request_list_page()

if __name__ == "__main__":
    main()