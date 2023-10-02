import time
from selenium import webdriver

# https://www.google-proxy.net/

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("chromedriver.exe", chrome_options=option)
url = r"https://www.google-proxy.net/"
driver.get(url)
# print(driver.page_source)
# driver.close()


try:
    for i in range(1, 1000):
        css_selector_raw = "#list > div > div.table-responsive > div > table > tbody > tr:nth-child(%s) > td:nth-child(%s)"
        https = driver.find_element_by_css_selector(css_selector_raw % (i, 7))
        # print(https.text)

        if https.text == "yes":
            ip = driver.find_element_by_css_selector(css_selector_raw % (i, 1))
            print(ip.text + ":", end="")

            port = driver.find_element_by_css_selector(css_selector_raw % (i, 2))
            print(port.text)
except Exception as e:
    # print("Exception: %s" % e)
    pass




