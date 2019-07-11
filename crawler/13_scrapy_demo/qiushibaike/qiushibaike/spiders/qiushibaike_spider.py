# -*- coding: utf-8 -*-
import scrapy


class QiushibaikeSpiderSpider(scrapy.Spider):
    name = 'qiushibaike_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        pass
