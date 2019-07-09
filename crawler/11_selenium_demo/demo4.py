from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 点击按钮
driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
submitTag = driver.find_element_by_id('su')
submitTag.click()

# 操作input
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
inputTag.clear()

# 操作checkbox
driver.get('https://www.douban.com/')

rememberBtn = driver.find_element_by_name('remember')
rememberBtn.click()

# 操作select
driver.get('https://news.hao123.com/wangzhi')

selectBtn = Select(driver.find_element_by_id('city-select'))
selectBtn.select_by_index(1)
selectBtn.select_by_value('上海')
selectBtn.select_by_visible_text('北京')