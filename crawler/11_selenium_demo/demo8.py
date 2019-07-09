from selenium import webdriver

driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

# driver.get('https://www.meowv.com/')
driver.execute_script("window.open('https://www.meowv.com/')")

print(driver.current_url)

print(driver.window_handles)

driver.switch_to_window(driver.window_handles[1])

print(driver.current_url)
print(driver.page_source)