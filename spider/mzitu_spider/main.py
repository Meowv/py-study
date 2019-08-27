# -*- coding: utf-8 -*-

import os
import re
import threading
from queue import Queue
from urllib import request

import requests
from lxml import etree
import time

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'referer': 'https://www.mzitu.com/'
}


class Procuder(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=HEADERS)
        html = etree.HTML(response.text)

        img_url = html.xpath("//div[@class='main-image']//img/@src")[0]
        img_name = html.xpath("//h2[@class='main-title']/text()")[0]
        if '（' not in img_name:
            img_name = img_name + '（1）'

        img_suffix = os.path.splitext(img_url)[1]

        filename = img_name + img_suffix

        self.img_queue.put((img_url, filename))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()

            print('开始下载：' + filename + '  URL：' + img_url)

            girl = requests.get(img_url, headers=HEADERS)
            if girl.status_code == 200 or girl.status_code == 304:
                with open('images/' + filename, 'wb') as f:
                    f.write(girl.content)


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)

    url = 'https://www.mzitu.com/hot/'

    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.text)

    # 获取最热板块页码最大值
    pages = html.xpath("//div[@class='nav-links']/a[last()-1]/text()")[0]

    for p in range(1, int(pages)):
        url = url + 'page/' + str(p)

        response_ = requests.get(url, headers=HEADERS)
        html_ = etree.HTML(response_.text)

        # 获取当前页的超链接
        links = html_.xpath("//ul[@id='pins']/li/a/@href")

        for link in links:
            response__ = requests.get(link, headers=HEADERS)
            html__ = etree.HTML(response__.text)

            # 详情页页码最大值
            max_page = html__.xpath(
                "//div[@class='pagenavi']/a[last()-1]/span/text()")[0]

            for current_page in range(1, int(max_page)):
                page_queue.put(link + '/' + str(current_page))

            t1 = Procuder(page_queue, img_queue)
            t2 = Consumer(page_queue, img_queue)
            t1.start()
            t2.start()


if __name__ == "__main__":
    main()
