# -*- coding: utf-8 -*-
import os
import sys
from time import sleep
from selenium import webdriver
# ChromeOptions = webdriver.ChromeOptions()
# ChromeOptions.add_argument('--headless')
# ChromeOptions.add_argument('--no-sandbox')
# ChromeOptions.add_argument('--disable-gpu')
# ChromeOptions.add_argument('--disable-dev-shm-usage')
# ChromeOptions.add_argument('window-size=1200x600')
from Options.Chrome_options import ChromeOptions
sys.path.append(os.path.dirname(__file__))

driver = webdriver.Chrome(options=ChromeOptions().options())
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
driver.find_element('id','kw').send_keys('xuzhu')
driver.find_element('id','su').click()
sleep(3)
driver.quit()

