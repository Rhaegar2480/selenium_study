from selenium import webdriver

# chrome drive download:
# https://googlechromelabs.github.io/chrome-for-testing/#stable


# driver = webdriver.Firefox()
# driver = webdriver.Safari()
driver = webdriver.Chrome("chromedriver.exe")
url = r"http://www.google.com"
driver.get(url)
# print(driver.page_source)

# 關閉瀏覽器視窗
# driver.close()



