# 載入必要的套件
import time
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

import csv
import random
import os


# 定義商品名稱
prod = '0050'


# 寫入標提列
file = open(prod + '_shareHolder.csv', "w", encoding="utf16")
file.write("日期, 證券代碼, 持股分級, 持股數量分級, 人數, 股數, 占集保庫存數比例% \n")

# 透過 selenium 進行爬蟲 找到瀏覽器核心
cur_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(cur_path, "chromedriver.exe")
print(chrome_driver_path)
s = Service(chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('disable-gpu')

# browser = webdriver.Chrome("chromedriver.exe", chrome_options=options)
browser = webdriver.Chrome(service=s)

# 進入集保網址
url = r"https://www.tdcc.com.tw/portal/zh/smWeb/qryStock"
browser.get(url)
time.sleep(3)

# 集保機制是採用，選擇最近的1周至50周，所以執行1-50的迴圈
for i in range(1, 3):
    # 除錯機制
    try:
        # 設定開啟網頁之日期 選定日期
        select_1 = Select(browser.find_element(By.NAME, "scaDate"))
        select_1.select_by_index(i)
        time.sleep(1)

        # 輸入股票代碼
        browser.find_element(By.ID, "StockNo").clear()
        browser.find_element(By.ID, "StockNo").send_keys(prod)
        time.sleep(1)

        # 模擬網頁送出查詢
        browser.find_element(By.XPATH, "//tr[4]//td[1]//input[1]").click()
        time.sleep(1)

        # 取得網頁原始碼
        html_file = browser.page_source

        # 建立beautifulSoup 解析文件
        soup = bs(html_file, "lxml")

        html_date = soup.find("span", class_="font")
        html_date = html_date.text
        html_date = html_date.split('：')[1]
        html_date = html_date.replace('年', '/').replace('月', '/').replace('日', '')
        print(html_date)

        # 找出回傳之分散表
        tbody = soup.find("table", class_="table").find("tbody").find_all("tr")

        # 每個股票的股權分散表的處理
        for tr in tbody:
            tds = tr.find_all("td")

            tmp_row = []
            for td in tds:
                tmp_row.append(td.text)
            tmp_row.insert(0, html_date)
            tmp_row.insert(1, prod)

            s = ','.join(tmp_row)+'\n'
            file.write(s)

        # 隨機休息 5-10秒
        time.sleep(random.randint(1, 5))

    except Exception as e:
        # print(prod, '有誤，請檢查程式', i)
        print("Exception: %s" % e)
        import sys
        sys.exit()
