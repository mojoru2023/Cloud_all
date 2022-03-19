# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 驱动路径
path = os.getcwd()
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)  # 参数添加

# 上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)
browser.maximize_window()
browser.save_screenshot('baidu.png')  # 捕获(截屏)保存

browser.quit()
