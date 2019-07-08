from selenium import webdriver
import time

driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.meowv.com/')

time.sleep(5)

# 关闭当前页面
driver.close()

# 退出整个浏览器
driver.quit()