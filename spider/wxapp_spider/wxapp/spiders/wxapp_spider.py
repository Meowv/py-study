# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wxapp.items import WxappItem


class WxappSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=%d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get() 
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath(".//a/text()").get()
        pubtime = author_p.xpath(".//span/text()").get()
        content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(content).strip()

        item = WxappItem(title=title, author=author, pubtime=pubtime, content=content)
        yield item
