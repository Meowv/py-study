# -*- coding: utf-8 -*-
import time

from scrapy import signals
from scrapy.http.response.html import HtmlResponse
from selenium import webdriver


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(3)

        try:
            while True:
                showMore = self.driver.find_element_by_class_name('show-more')
                showMore.click()
                time.sleep(0.5)
                if not showMore:
                    break
        except:
            pass

        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response
