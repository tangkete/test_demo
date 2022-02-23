# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument('--headless')
ChromeOptions.add_argument('--no-sandbox')
ChromeOptions.add_argument('--disable-gpu')
ChromeOptions.add_argument('--disable-dev-shm-usage')
ChromeOptions.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=ChromeOptions)
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
driver.find_element('id','kw').send_keys('xuzhu')
driver.find_element('id','su').click()
sleep(3)
driver.quit()
