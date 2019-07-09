from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()