# -*- coding: utf-8 -*-
from urllib import request

import scrapy
from PIL import Image


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    profile_url = 'https://www.douban.com/people/149890918/'
    edit_signature_url = 'https://www.douban.com/j/people/149890918/edit_signature'

    def parse(self, response):
        formdata = {
            'name': '...',
            'password': '...',
            'remember': 'false',
        }

        # captcha_url = response.css('img#captcha_image::attr(src)').get()
        # if captcha_url:
        #     captcha = self.regonize_captcha(captcha_url)
        #     formdata['captcha-solution'] = captcha
        #     captcha_id = response.xpath("//input[@name='captcha-id']/@value").get()
        #     formdata['captcha-id'] = captcha_id

        yield scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=self.parse_login)

    def parse_login(self, response):
        # if response.url == 'https://www.douban.com/':
        if 'success' in response.text:
            print("login success ...")
            yield scrapy.Request(self.profile_url, callback=self.parse_profile)
        else:
            print("login failed ...")

    def parse_profile(self, response):
        print(response.url)
        if response.url == self.profile_url:
            ck = response.xpath("//input[@name='ck']/@value").get()
            print(ck)
            formdata = {
                'ck': ck,
                'signature': '啦啦啦啦啦啦啦啦啦啦~~'
            }
            yield scrapy.FormRequest(self.edit_signature_url, formdata=formdata)
        else:
            print("error...")

    def regonize_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input("请输入验证码：")
        return captcha
