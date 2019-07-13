# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jannshu_spider.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title =  response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//div[@class='info']/span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        origin_url = response.url
        article_id = origin_url.split('?')[0].split('/')[-1]
        content = response.xpath("//div[@class='show-content']/div").get()

        item = ArticleItem(
            title = title,
            avatar = avatar,
            author = author,
            pub_time = pub_time,
            article_id = article_id,
            origin_url = origin_url,
            content = content
        )
        yield item
