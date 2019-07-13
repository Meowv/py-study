# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from boss.items import BossItem


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    rules = (
        # 匹配职位列表页规则
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        # 匹配职位详情页规则
        Rule(LinkExtractor(allow=r'.+job_detail/.+.html'), callback="parse_job", follow=False),
    )

    def parse_job(self, response):
        name = response.xpath("//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='name']/span[@class='salary']/text()").get().strip()
        infos = response.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/p//text()").getall()
        city = infos[0]
        work_years = infos[1]
        education = infos[2]
        company = response.xpath("//a[@ka='job-detail-company_custompage']/text()").get().strip()
        desc = response.xpath("//div[@class='job-sec']/div[@class='text']//text()").getall()
        desc = "\n".join(desc).strip()

        item = BossItem(name=name,salary=salary,city=city,work_years=work_years,education=education,company=company,desc=desc)
        yield item
