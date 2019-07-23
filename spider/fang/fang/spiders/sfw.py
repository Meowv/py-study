# -*- coding: utf-8 -*-

import scrapy
import re
from fang.items import NewHouseItem


class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    # 房天下新房和二手房数据爬取
    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            provinces_td = tds[0]
            province_text = provinces_td.xpath(".//text()").get()
            province_text = re.sub(r'\s', '', province_text)
            if province_text:
                province = province_text

            # 不爬取海外房源
            if province == '其它':
                continue

            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()

                # 构建新房url链接 eg:https://sh.newhouse.fang.com/house/s/
                city_url_list = list(city_url)
                dot_index = city_url_list.index('.')
                city_url_list.insert(dot_index, '.newhouse')
                newhouse_url = "".join(city_url_list) + 'house/s/'
                # 北京例外，单独指定
                if 'bj.' in newhouse_url:
                    newhouse_url = 'https://newhouse.fang.com/house/s/'

                # 构建二手房url链接  eg:https://sh.esf.fang.com/
                city_url_list = list(city_url)
                dot_index = city_url_list.index('.')
                city_url_list.insert(dot_index, '.esf')
                esf_url = "".join(city_url_list)
                # 北京例外，单独指定
                if 'bj.' in esf_url:
                    esf_url = 'https://esf.fang.com/'

                print("省份", province)
                print("省份", city)
                print("新房链接", newhouse_url)
                print("二手房链接", esf_url)
                print("~"*100)

                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info": (province, city)})

                yield scrapy.Request(url=esf_url, callable=self.parse_esf, meta={"info": (province, city)})
                break
            break

    # 新房解析
    def parse_newhouse(self, response):
        province, city = response.meta.get('info')

        lis = response.xpath("//div[@id='newhouse_loupai_list']/ul/li")
        for li in lis:
            try:
                name = li.xpath(
                    ".//div[@class='nlcd_name']/a/text()").get().strip()
                house_type_list = li.xpath(
                    ".//div[contains(@class,'house_type')]/a/text()").getall()
                house_type_list = list(
                    map(lambda x: re.sub(r'\s', '', x), house_type_list))
                rooms = list(
                    filter(lambda x: x.endswith('居'), house_type_list))
                area = "".join(li.xpath(
                    ".//div[contains(@class, 'house_type')]/text()").getall())
                area = re.sub(r'\s|－|/', '', area)
                address = li.xpath(".//div[@class='address']/a/@title").get()
                district_text = "".join(
                    li.xpath(".//div[@class='address']/a//text()").getall())
                district = re.search(r'.*\[(.+)\].*', district_text).group(1)
                sale = li.xpath(
                    ".//div[contains(@class, 'fangyuan')]/span/text()").get()

                price = "".join(
                    li.xpath(".//div[@class='nhouse_price']//text()").getall())
                price = re.sub(r'\s|广告', '', price)

                origin_url = li.xpath(
                    ".//div[@class='nlcd_name']/a/@href").get()

                item = NewHouseItem(name=name, rooms=rooms, area=area, district=district,
                                    sale=sale, price=price, origin_url=origin_url, province=province, city=city)
                yield item

            except:
                pass
        next_url = response.xpath(
            "//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, meta={"info": (province, city)})

    # 二手房解析
    def parse_esf(self, response):
        province, city = response.meta.get('info')
        pass
