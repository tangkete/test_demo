# -*- coding: utf-8 -*-
import time
from functools import wraps
'''
    自定义web框架：
    1、根据请求路径，动态响应对应的数据
    2、如果请求路径没有对应的响应数据，也需要返回404
    3、
'''


# 定义路由表,
route_list = []
# route_list = {
#     ('/index.html', index),
#     ('/userinfo.html', user_info)
# }

# 定义一个带参数的装饰器
def requests_route(requests_path):
    def add_route(func):
        # 添加到路由表, 请求路径和请求方法：('/userinfo.html', user_info)
        route_list.append((requests_path, func))
        @wraps(func)
        def invoke(*args, **kwargs):
            return func() # user_info()
        return invoke
    return add_route



def respon_header(response_body, response_type='text/html'):
    """
    :param response_body: 响应主体
    :param response_type: 响应类型
    :return:
    """
    response_header = 'Content-Length: ' + str(len(response_body)) + '\r\n' \
                      + 'Content-Type: '+response_type+'; charset=UTF-8\r\n' \
                      + 'Date: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\r\n' \
                      + 'Server: MyServer\r\n'
    return response_header


# 处理动态资源请求的函数
def handle_request(params):
    request_path = params['request_path']
    for path,func in route_list:
        if request_path == path:
            return func()
    else:
        return page_not_found()

    # 存在路由表则不需要if判断
    # if request_path == '/index.html':  #首页
    #     response = index()
    #     return response
    # elif request_path == '/userinfo.html': #个人中心
    #     response = user_info()
    #     return response
    # else:
    #     return page_not_found()


@requests_route('/userinfo.html')
def user_info():
    """
    处理userinfo.html的动态请求
    :return:
    """
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open('template/user_info.html', 'r', encoding='utf-8') as f:
        response_body = f.read()
    response_body = response_body.replace('{%dates%}',date)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = respon_header(response_body)
    response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body.encode('utf-8')
    return response

# 当前index 函数， 专门处理index.html请求
@requests_route('/index.html')
def index():
    # 动态资源， 例：系统时间显示在页面,
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # response_body = data
    with open('template/index.html', 'r', encoding='utf-8') as f:
        response_body = f.read()
    response_body = response_body.replace('{%dates%}',date)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = respon_header(response_body)
    response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body.encode('utf-8')
    return response


def page_not_found():
    with open('static/404.html', 'rb') as f:
        response_body = f.read()  # 响应的主体页面（字节）
    # 返回响应头（字符）
    response_first_line = 'HTTP/1.1 404 Not Found\r\n'
    response_header = respon_header(response_body)
    response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body
    return response




