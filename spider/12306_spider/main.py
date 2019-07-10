# 使用 selenium + Chromedriver 实现12306抢票
# 1. 让浏览器打开12306登录界面，然后手动进行登录
# 2. 登录完成后让浏览器跳转到购票界面
# 3. 手动输入出发地、目的地、出发日期，然后检测到输入完成后找到查询按钮，执行点击事件，进行车次查询
# 4. 查找想要抢票的车次是否有余票(有、数字)，找到对应的预订按钮，执行点击事件，如果没有出现以上两个(有、数字)，那么就循环查询操作
# 5. 检测到有票()，那么执行预订按钮的点击事件，来到预订的界面后，选择乘客的checkbox，然后执行点击事件，再找到提交订单按钮执行点击事件
# 6. 点击完提交订单按钮后，会弹出确认的对话框，然后找到 "确认" 按钮执行点击事件，完成抢票。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class spider_12306():
    driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'

    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.init_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.passenger_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        self.driver = webdriver.Chrome(executable_path = spider_12306.driver_path)

    def _write_input(self):
        self.from_station = input('出发地: ')
        self.to_station = input('目的地: ')
        # 时间格式: yyyy-MM-dd
        self.depart_time = input('出发日: ')
        self.passengers = input('乘客姓名(如果多个乘客,用英文逗号隔开): ').split(',')
        self.trains = input('车次(如果有多个车次，用英文逗号隔开): ').split(',')

    def _login(self):
        self.driver.get(self.login_url)
        
        WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.init_url))
        print("登录成功...")

        self._order_ticket()

    def _order_ticket(self):
        # 1. 跳转到查票的界面
        self.driver.get(self.search_url)
        # 2. 等待出发地是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.from_station)
        )
        # 3. 等待目的地是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.to_station)
        )
        # 4. 等待出发日是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self.depart_time)
        )
        # 5. 等待查询按钮是否可以点击
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket'))
        )
        # 6. 如果能被点击，执行点击事件
        searchBtn = self.driver.find_element_by_id('query_ticket')
        searchBtn.click()
        # 7. 点击查询按钮以后，等待车次信息是否显示出来了
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, './/tbody[@id="queryLeftTable"]/tr'))
        )
        # 8. 出现车次信息后，找到想要的车次信息
        tr_list = self.driver.find_elements_by_xpath('.//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        # 9. 遍历所有车次列表
        for tr in tr_list:
            train_number = tr.find_element_by_class_name('number').text
            if train_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                if left_ticket == '有' or left_ticket.isdigit:
                    print(train_number + "有票")
                    orderBtn = tr.find_element_by_class_name('btn72')
                    orderBtn.click()

                    # 等待是否跳转到确认乘客的页面
                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.passenger_url)
                    )
    
    def run(self):
        self._write_input()
        self._login()
        self._order_ticket()

if __name__ == "__main__":
    spider = spider_12306()
    spider.run()
