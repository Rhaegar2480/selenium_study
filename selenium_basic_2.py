import time
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
url = r"http://www.google.com"
driver.get(url)
# print(driver.page_source)

# 關閉瀏覽器視窗
# driver.close()

# 定位搜尋框
element = driver.find_element_by_class_name("gLFyf")

# 傳入字串
element.send_keys("123456")
# 清除網頁元素原先的字串或搜索詞
# element.clear()

button = driver.find_element_by_class_name("gNO89b")
button.click()
