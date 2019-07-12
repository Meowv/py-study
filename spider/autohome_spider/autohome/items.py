# -*- coding: utf-8 -*-

import scrapy


class AutohomeItem(scrapy.Item):
    category = scrapy.Field()
    urls = scrapy.Field()
