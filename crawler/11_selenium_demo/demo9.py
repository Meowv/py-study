from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://27.43.190.191:9999')

driver_path = r'D:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.get('http://www.httpbin.org/ip')

print(driver.page_source)