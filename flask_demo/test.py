# -*- coding: utf-8 -*-
from socket import *
import threading
import os
import time

"""
    web服务器：
    1、接收客户端http请求，底层是TCP
    2、判断是静态请求还是动态请求
    3、如果静态资源怎么处理
    4、如果动态资源怎么处理
    5、关闭web服务器
"""

class WebServer(object):

    def __init__(self,post):

        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)  # 允许端口复用
        server_socket.bind(('', post))  # 绑定端口
        server_socket.listen(128)  # 监听端口
        self.server_socket = server_socket


    def handle_browser_request(self, new_socket):
        recv_data = new_socket.recv(2048)
        if len(recv_data) == 0:
            new_socket.close()
            return
        requests_date = recv_data.decode('utf-8')
        # print("当前接收的请求数据:\r\n",requests_date)
        requests_path = requests_date.split(' ', maxsplit=2)[1]
        print(requests_path)
        if requests_path == '/':
            requests_path = '/index.html'

        if requests_path.endswith(('.html')):
            pass



    def start(self):
        while True:
            new_socket, ip_post = self.server_socket.accept()
            sub_thering = threading.Thread(target=self.handle_browser_request, args=(new_socket,))
            sub_thering.setDaemon(True)
            sub_thering.start()


if __name__ == '__main__':
    web_server = WebServer(8899)
    web_server.start()
