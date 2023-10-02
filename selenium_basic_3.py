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


# """Set of special keys codes."""
# NULL = '\ue000'
# CANCEL = '\ue001' # ^break
# HELP = '\ue002'
# BACKSPACE = '\ue003'
# BACK_SPACE = BACKSPACE
# TAB = '\ue004'
# CLEAR = '\ue005'
# RETURN = '\ue006'
# ENTER = '\ue007'
# SHIFT = '\ue008'
# LEFT_SHIFT = SHIFT
# CONTROL = '\ue009'
# LEFT_CONTROL = CONTROL
# ALT = '\ue00a'
# LEFT_ALT = ALT
# PAUSE = '\ue00b'
# ESCAPE = '\ue00c'
# SPACE = '\ue00d'
# PAGE_UP = '\ue00e'
# PAGE_DOWN = '\ue00f'
# END = '\ue010'
# HOME = '\ue011'
# LEFT = '\ue012'
# ARROW_LEFT = LEFT
# UP = '\ue013'
# ARROW_UP = UP
# RIGHT = '\ue014'
# ARROW_RIGHT = RIGHT
# DOWN = '\ue015'
# ARROW_DOWN = DOWN
# INSERT = '\ue016'
# DELETE = '\ue017'
# SEMICOLON = '\ue018'
# EQUALS = '\ue019'
# NUMPAD0 = '\ue01a' # number pad keys
# NUMPAD1 = '\ue01b'
# NUMPAD2 = '\ue01c'
# NUMPAD3 = '\ue01d'
# NUMPAD4 = '\ue01e'
# NUMPAD5 = '\ue01f'
# NUMPAD6 = '\ue020'
# NUMPAD7 = '\ue021'
# NUMPAD8 = '\ue022'
# NUMPAD9 = '\ue023'
# MULTIPLY = '\ue024'
# ADD = '\ue025'
# SEPARATOR = '\ue026'
# SUBTRACT = '\ue027'
# DECIMAL = '\ue028'
# DIVIDE = '\ue029'
# F1 = '\ue031' # function keys
# F2 = '\ue032'
# F3 = '\ue033'
# F4 = '\ue034'
# F5 = '\ue035'
# F6 = '\ue036'
# F7 = '\ue037'
# F8 = '\ue038'
# F9 = '\ue039'
# F10 = '\ue03a'
# F11 = '\ue03b'
# F12 = '\ue03c'
# META = '\ue03d'
# COMMAND = '\ue03d' 

# ctrl + c, ctrl + v
# element.send_keys(Keys.CONTROL, "c")
# element.send_keys(Keys.CONTROL, "v")

# 下/上 一項瀏覽紀錄
# driver.forward()
# driver.back()