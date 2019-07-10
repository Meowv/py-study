# 使用 selenium + Chromedriver 实现12306抢票
# 1. 让浏览器打开12306登录界面，然后手动进行登录
# 2. 登录完成后让浏览器跳转到购票界面
# 3. 手动输入出发地、目的地、出发日期，然后检测到输入完成后找到查询按钮，执行点击事件，进行车次查询
# 4. 查找想要抢票的车次是否有余票(有、数字)，找到对应的预订按钮，执行点击事件，如果没有出现以上两个(有、数字)，那么就循环查询操作
# 5. 检测到有票()，那么执行预订按钮的点击事件，来到预订的界面后，选择乘客的checkbox，然后执行点击事件，再找到提交订单按钮执行点击事件
# 6. 点击完提交订单按钮后，会弹出确认的对话框，然后找到 "确认" 按钮执行点击事件，完成抢票。

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class spider_12306():
    driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'

    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.init_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.driver = webdriver.Chrome(executable_path = spider_12306.driver_path)

    def _login(self):
        self.driver.get(self.login_url)
       
        WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.init_url))
        print("登录成功...")

    def _order_ticket(self):
        pass
    
    def run(self):
        self._login()
        self._order_ticket()

if __name__ == "__main__":
    spider = spider_12306()
    spider.run()
