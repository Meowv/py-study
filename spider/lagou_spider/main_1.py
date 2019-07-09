import re
import time

import requests
from lxml import etree

headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome75.0.3770.100 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_cookies(url):
    session = requests.Session()
    session.get(url, headers=headers)
    cookie = session.cookies
    return cookie

def request_list_page():
    page_url = 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    data = {
        'first': 'false',
        'pn': 1,
        'kd': 'python'
    }

    for x in range(1, 10):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data, cookies=get_cookies(page_url))
        result = response.json()
        positons = result['content']['positionResult']['result']
        for x in positons:
            positonId = x['positionId']
            positon_url = 'https://www.lagou.com/jobs/%d.html' % positonId
            parse_positon_detail(positon_url)

def parse_positon_detail(url):
    headers["Upgrade-Insecure-Requests"] = '1'

    response = requests.get(url,headers=headers, cookies=get_cookies(url))
    text = response.text
    html = etree.HTML(text)

    # 职位名称
    position_name = html.xpath("//h2[@class='name']/text()")[0]

    job_request_spans = html.xpath("//dd[@class='job_request']//span")

    # 薪资
    salary = job_request_spans[0].xpath('.//text()')[0].strip()

    # 城市
    city = job_request_spans[1].xpath('.//text()')[0].strip()
    city = re.sub(r'[\s/]', '', city)

    # 工作经验
    work_year = job_request_spans[2].xpath('.//text()')[0].strip()
    work_year = re.sub(r'[\s/]', '', work_year)

    # 学历
    education = job_request_spans[3].xpath('.//text()')[0].strip()
    education = re.sub(r'[\s/]', '', education)

    # 职位描述
    desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()

    print(position_name)
    print(salary)
    print(city)
    print(work_year)
    print(education)
    print(desc)

def main():
    request_list_page()

if __name__ == "__main__":
    main()
