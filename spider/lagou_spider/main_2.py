import re
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LagouSpider(object):
    driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='
        self.positions = []

    def run(self):
        while True:
            self.driver.get(self.url)
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            )
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            if "pager_next_disabled" in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()
            time.sleep(1)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']/h2[@class='name']"))
        )
        source = self.driver.page_source
        self.parse_detail_page(source)
        # 关闭当前的详情页
        self.driver.close()
        # 继续切换回列表页
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        # 职位名称
        position_name = html.xpath("//h2[@class='name']/text()")[0]

        # 公司名称
        company = html.xpath("//h3[@class='fl']/text()")[0].strip()

        job_request_spans = html.xpath("//dd[@class='job_request']//span")

        # 薪资
        salary = job_request_spans[0].xpath('.//text()')[0].strip()

        # 城市
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)

        # 工作经验
        work_year = job_request_spans[2].xpath('.//text()')[0].strip()
        work_year = re.sub(r'[\s/]', '', work_year)

        # 学历
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r'[\s/]', '', education)

        # 职位描述
        desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()

        position = {
            'name': position_name,
            'company': company,
            'salary': salary,
            'city': city,
            'work_year': work_year,
            'education': education,
            'desc': desc
        }
        self.positions.append(position)
        print(position)
        print('~'*100)

if __name__ == "__main__":
    spider = LagouSpider()
    spider.run()
