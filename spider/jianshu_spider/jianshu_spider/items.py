# -*- coding: utf-8 -*-
import scrapy


class ArticleItem(scrapy.Item):
    article_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    origin_url = scrapy.Field()
    author = scrapy.Field()
    avatar = scrapy.Field()
    pub_time = scrapy.Field()
    read_count = scrapy.Field()
    like_count = scrapy.Field()
    word_count = scrapy.Field()
    subjects = scrapy.Field()
    comments_count = scrapy.Field()
