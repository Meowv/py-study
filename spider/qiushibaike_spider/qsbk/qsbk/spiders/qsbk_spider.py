# -*- coding: utf-8 -*-
import scrapy


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        duanziDivs = contentLeft = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanziDivs:
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            contnet = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            contnet = "".join(contnet).strip()
            
            
