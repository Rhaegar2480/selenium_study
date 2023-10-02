import time
from selenium import webdriver

# https://geonode.com/free-proxy-list
# 點下button 下載json
# => 沒有 https

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome("chromedriver.exe", chrome_options=option)
driver = webdriver.Chrome("chromedriver.exe")
url = r"https://geonode.com/free-proxy-list"
driver.get(url)
# print(driver.page_source)
# driver.close()


css_selector = "#__next > div > div > div:nth-child(1) > div > section > div > div.relative.block.lg\:flex.items-start.justify-center.gap-8.max-w-\[1550px\].mx-auto > div.lg\:w-\[calc\(100vw-320px\)\] > div > div.sticky.top-0.rounded-t-lg.z-10.bg-supportSecondary-200.border-b.border-1.border-secondary-50.overflow-hidden > div.flex.gap-4.py-5.px-4 > div.flex.w-full.lg\:w-auto > div > div.flex.w-full.flex-col.lg\:flex-row.gap-3.text > div > button"
button = driver.find_element_by_css_selector(css_selector)
button.click()
time.sleep(10)
driver.close()




