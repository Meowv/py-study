# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from jianshu_spider.items import ArticleItem


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
        word_count = response.xpath("//span[@class='wordage']/texe()").get()
        read_count = response.xpath("//span[@class='views-count']/texe()").get()
        like_count = response.xpath("//span[@class='likes-count']/texe()").get()
        comments_count = response.xpath("//span[@class='comments-count']/texe()").get()
        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = ArticleItem(
            title = title,
            avatar = avatar,
            author = author,
            pub_time = pub_time,
            article_id = article_id,
            origin_url = origin_url,
            content = content,
            word_count = word_count,
            read_count = read_count,
            like_count = like_count,
            comments_count = comments_count,
            subjects = subjects
        )
        yield item
