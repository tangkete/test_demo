# -*- coding: utf-8 -*-
import time
'''
    自定义web框架：
    1、根据请求路径，动态响应对应的数据
    2、如果请求路径没有对应的响应数据，也需要返回404
    3、
'''

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
    response_header = 'Content-Length: ' + str(len(response_body)) + '\r\n' \
                      + 'Content-Type: text/html; charset=UTF-8\r\n' \
                      + 'Date: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\r\n' \
                      + 'Server: MyServer\r\n'
    response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body.encode('utf-8')
    return response

# 当前index 函数， 专门处理index.html请求
def index():
    # 动态资源， 例：系统时间显示在页面,
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # response_body = data
    with open('template/index.html', 'r', encoding='utf-8') as f:
        response_body = f.read()
    response_body = response_body.replace('{%dates%}',date)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = 'Content-Length: ' + str(len(response_body)) + '\r\n' \
                      + 'Content-Type: text/html; charset=UTF-8\r\n' \
                      + 'Date: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\r\n' \
                      + 'Server: MyServer\r\n'
    response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body.encode('utf-8')
    return response


def page_not_found():
    with open('static/404.html', 'rb') as f:
        response_body = f.read()  # 响应的主体页面（字节）
    # 返回响应头（字符）
    response_first_line = 'HTTP/1.1 404 Not Found\r\n'
    response_header = 'Content-Length: ' + str(len(response_body)) + '\r\n' \
                      + 'Content-Type: text/html; charset=UTF-8\r\n' \
                      + 'Date: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\r\n' \
                      + 'Server: MyServer\r\n'
    response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body
    return response



# 定义路由表,用二元组
route_list = {
    ('/index.html', index),
    ('/userinfo.html', user_info)
}
