# -*- coding: utf-8 -*-
import os
import sys
from time import sleep
from selenium import webdriver
sys.path.append(os.path.dirname(__file__))

option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--disable-gpu')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--headless')

# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
# # 给浏览器定义cookie
driver.add_cookie({'name':'a_lang',
                   'value':'zh-hans-cn',
                   'domain':'www.baidu.com',
                   })
driver.find_element('id','kw').send_keys('xuzhu')
driver.find_element('id','su').click()
sleep(3)
# 获取浏览器的cookie
cooike = driver.get_cookie('a_lang')
print(cooike)
driver.quit()

