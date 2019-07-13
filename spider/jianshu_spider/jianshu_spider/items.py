# -*- coding: utf-8 -*-
import scrapy


class ArticleItem(scrapy.Item):
    article_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    origin_url = scrapy.Field()
    author = scrapy.Field()
    avator = scrapy.Field()
    pub_time = scrapy.Field()
