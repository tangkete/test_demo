# -*- coding: utf-8 -*-
from selenium import webdriver


class ChromeOptions:
    def options(self):
        # chrome浏览器的配置项，可以通过修改默认参数，改变默认启动的浏览器的形态
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1200x600')
        # 将浏览器默认设置为最大窗体
        # options.add_argument('start-maximized')
        # 设置默认窗体的启动大小
        # options.add_argument('window-size=400,2000')
        # 无头模式：虽然看不到，但是一切照旧，在一些特定场景下会失败
        options.add_argument('--headless')
        # 去掉默认的提示自动化信息：没啥用，一般没有什么影响。警告条可能会导致页面内容的遮挡或者挤压，影响自动化测试
        # options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        # 去掉控制台多余信息
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # 老版本去掉警告条的参数，已经不生效了。已弃用
        # options.add_argument('disable-infobars')
        # 读取本地缓存，实现一个有缓存的浏览器，这个指令执行前必须关闭所有本地的chrome浏览器
        # options.add_argument(r'--user-data-dir=C:\Users\xuzhu\AppData\Local\Google\Chrome\User Data')
        # 去掉账号密码弹窗
        # prefs = {}
        # prefs["credentials-enable-service"] = False
        # prefs['profile.password_manager_enable'] = False
        # options.add_experimental_option("prefs", prefs)

        # 娱乐设置
        # 指定窗口打开在哪个位置
        # options.add_argument('window-position=2200,500')
        # 隐身模式
        # options.add_argument('incognito')
        # 去掉控制台打印的多余信息：忽略！暂时参数有问题
        # options.add_argument("--disable-gpu")
        # options.add_argument("--log_level= 3")
        # options.add_argument("--ignore-certificate-errors")
        return options
