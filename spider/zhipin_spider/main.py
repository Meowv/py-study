import csv
import re
import time
from urllib import request

import pytesseract
from lxml import etree
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BossSpider(object):
    driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
    def __init__(self):
        # pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

        self.driver = webdriver.Chrome(executable_path=BossSpider.driver_path)
        self.url = 'https://www.zhipin.com/job_detail/?query=python&city=101020100&industry=&position='
        self.domain = 'https://www.zhipin.com'

        fp = open('boss.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(fp, ['name', 'company', 'salary', 'city', 'work_years', 'education', 'desc'])
        self.writer.writeheader()

    def run(self):
        while True:
            self.driver.get(self.url)
            # if len(self.driver.find_element_by_id('captcha')) > 0:
            #     self.fill_capycha()
            #     time.sleep(2)
            #     continue
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='page']/a[last()]"))
            )
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//div[@class='page']/a[last()]")
            if 'disabled' in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()
            time.sleep(1)

    def fill_capycha(self):
        captchaInput = self.driver.find_element_by_id('capycha')
        captchaImg = self.driver.find_elements_by_class_name('code')
        submitBtn = self.driver.find_element_by_class_name('btn')
        src = captchaImg.get_attribute('src')
        request.urlretrieve(self.domain + src, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        captcha = re.sub(r'[\s/]', '', text)
        captchaInput.send_keys(captcha)
        submitBtn.click()

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//div[@class='info-primary']/h3[@class='name']/a/@href")
        for link in links:
            url = self.domain + link
            self.request_detail_page(url)
            time.sleep(1)

    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='info-primary']/div[@class='name']"))
        )
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        name = html.xpath("//div[@class='name']/text()")[0].strip()
        salary = html.xpath("//div[@class='name']/span[@class='salary']/text()")[0].strip()
        infos = html.xpath("//div[@class='info-primary']/p//text()")
        city = infos[0]
        work_years = infos[1]
        education = infos[2]
        company = html.xpath("//a[@ka='job-detail-company_custompage']/text()")[0].strip()
        desc = html.xpath("//div[@class='job-sec']/div[@class='text']//text()")
        desc = "\n".join(desc).strip()
        position = {
            'name': name,
            'company': company,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.write_position(position)

    def write_position(self, position):
        self.writer.writerow(position)
        print(position)

if __name__ == "__main__":
    spider = BossSpider()
    spider.run()
