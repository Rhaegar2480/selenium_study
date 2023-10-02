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

from selenium import webdriver
from selenium.webdriver.common.by import By

# id
# 使用By方法
driver.find_element(By.ID, "example")    # 抓取第一個
driver.find_elements(By.ID, "example")   # 抓取所有
# 直接使用函數
driver.find_element_by_id("example")     # 抓取第一個
driver.find_elements_by_id("example")    # 抓取所有


# classname
# 使用By方法
driver.find_element(By.CLASS_NAME, "example")    # 抓取第一個
driver.find_elements(By.CLASS_NAME, "example")   # 抓取所有
# 直接使用函數
driver.find_element_by_class_name("example")     # 抓取第一個
driver.find_elements_by_class_name("example")    # 抓取所有

# class= "hp vasp"
# 字串內有空格的話要改為 . => hp vasq改為 hp.vasq
driver.find_element(By.CLASS_NAME, "hp.vasq")
driver.find_element_by_class_name("hp.vasq")



# name
# 使用NAME查找網頁元素 # 抓取第一個
driver.find_element(By.NAME, "csi")
driver.find_element_by_name("csi")



# link_text
# 使用LINK_TEXT查找網頁元素 # 抓取第一個
driver.find_element(By.LINK_TEXT, "關於 Google")
driver.find_element_by_link_text("關於 Google")


# partial_link_text
# 類似於LINK_TEXT方法，但只需要部份文字即可
# 使用PARTIAL_LINK_TEXT查找網頁元素 # 抓取第一個
driver.find_element(By.PARTIAL_LINK_TEXT, "Google")
driver.find_element_by_partial_link_text("Google")

# 抓取所有 並指定索引
driver.find_elements(By.PARTIAL_LINK_TEXT, "Google")[1]
driver.find_elements_by_partial_link_text("Google")[1]


# tag_name
# tag即是HTML網頁標籤，是網頁檢視器裡紫色的字元部分
# 將網頁結構劃歸為各個階層，如 head、body、style、div

# TAG選擇器特別要注意的是，HTML標籤時常重複，因此TAG選擇器通常適用於抓取大框架的網頁元素再做細部搜尋
driver.find_element(By.TAG_NAME, "head")
driver.find_element_by_tag_name("head")



# xpath
# XPath是用於在XML文檔中定位節點的語言
# XPath以絕對路徑（不建議使用，超級容易失敗，要不斷維護）定位元素
# 在內容上點擊右鍵 → Copy → Copy (full) XPath，獲取絕對或相對XPath
driver.find_element(By.XPATH, '//*[@id="hptl"]/a[1]')
driver.find_element_by_xpath('//*[@id="hptl"]/a[1]')


# css_selector
# 想定位的網頁元素沒有唯一的ID(或其他)，則推薦使用CSS SELECTOR來查找元素
# 「/」改寫成「>」
# XPath: //div/a
# CSS: div > a

# 「//」改寫成「 (空格)」
# XPath: //div//a
# CSS: div a

# 用id查找「#」
# XPath: //div[@id=’example’]
# CSS: #example

# 用classname查找「.」
# XPath: //div[@class=’example’]
# CSS: .example






















