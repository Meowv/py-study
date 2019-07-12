# -*- coding: utf-8 -*-

import scrapy


class AutohomeItem(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()