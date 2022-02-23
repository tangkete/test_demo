# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from Options.Chrome_options import ChromeOptions

driver = webdriver.Chrome(options=ChromeOptions().options())
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
driver.find_element('id','kw').send_keys('xuzhu')
driver.find_element('id','su').click()
sleep(3)
driver.quit()
