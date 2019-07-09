from selenium import webdriver
from lxml import etree

driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# html = etree.HTML(driver.page_source)
# html.xpath("")

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
# inputTag = driver.find_element_by_css_selector('.quickdelete-wrap > input')

inputTag = driver.find_elements_by_css_selector('.quickdelete-wrap > input')[0]

inputTag.send_keys('python')