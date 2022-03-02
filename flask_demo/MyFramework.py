# -*- coding: utf-8 -*-
'''
    自定义web框架：
    1、根据请求路径，动态响应对应的数据
    2、如果请求路径没有对应的响应数据，也需要返回404
    3、
'''

# 处理动态资源请求的函数
def handle_request(params):
    request_path = params['request_path']
    if request_path == '/index.html':
        response = index()
        return response
    else:
        pass


# 当前index 函数， 专门处理index.html请求
def index():
    pass
