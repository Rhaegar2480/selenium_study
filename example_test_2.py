import time
from selenium import webdriver

# http://free-proxy.cz/en/
# http://free-proxy.cz/en/proxylist/country/all/https/date/all

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("chromedriver.exe", chrome_options=option)
url = r"http://free-proxy.cz/en/proxylist/country/all/https/date/all"
driver.get(url)
# print(driver.page_source)
# driver.close()



for i in range(1, 11):
    for j in range(1, 3):
        css_selector = "#proxy_list > tbody > tr:nth-child(%s) > td:nth-child(%s)" % (i, j)
        ip = driver.find_element_by_css_selector(css_selector)
        print(ip.text + " ", end="")
    print()





