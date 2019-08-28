# -*- coding: utf-8 -*-

import os
import requests
from lxml import etree
import time

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'referer': 'https://www.mzitu.com/'
}


def main():
    url = 'https://www.mzitu.com/hot/'

    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.text)

    # 获取最热板块页码最大值
    pages = html.xpath("//div[@class='nav-links']/a[last()-1]/text()")[0]

    for p in range(1, int(pages)):
        _url = url + 'page/' + str(p)

        _response = requests.get(_url, headers=HEADERS)
        html = etree.HTML(_response.text)

        # 获取当前页的超链接
        links = html.xpath("//ul[@id='pins']/li/a/@href")

        for link in links:
            _response = requests.get(link, headers=HEADERS)
            html = etree.HTML(_response.text)

            # 详情页页码最大值
            max_page = html.xpath(
                "//div[@class='pagenavi']/a[last()-1]/span/text()")[0]

            for current_page in range(1, int(max_page)):
                url = link + '/' + str(current_page)
                parse_page(url)
                time.sleep(1)


def parse_page(url):
    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.text)

    img_url = html.xpath("//div[@class='main-image']//img/@src")[0]
    img_name = html.xpath("//h2[@class='main-title']/text()")[0]
    if '（' not in img_name:
        img_name = img_name + '（1）'

    img_suffix = os.path.splitext(img_url)[1]

    filename = img_name + img_suffix
    download(img_url, filename)


def download(img_url, filename):
    print('开始下载：' + filename + '  URL：' + img_url)

    girl = requests.get(img_url, headers=HEADERS)
    if girl.status_code == 200 or girl.status_code == 304:
        with open('images/' + filename, 'wb') as f:
            f.write(girl.content)


if __name__ == "__main__":
    main()
