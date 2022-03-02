# -*- coding: utf-8 -*-
"""
    web服务器：
    1、接收客户端http请求，底层是TCP
    2、判断是静态请求还是动态请求
    3、如果静态资源怎么处理
    4、如果动态资源怎么处理
    5、关闭web服务器
"""
import socket
import sys
import threading
import time
import MyFramework

# web服务器主类
class MyHttpWebServer(object):

    def __init__(self, post):
        # 初始化创建http服务的socket
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置允许端口号复用，主要SO_REUSEADDR
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        socket_server.bind(('', post))
        # 监听端口设置线程最大等待个数
        socket_server.listen(128)
        self.socket_server = socket_server

    @staticmethod
    def handle_browser_request(new_socket):
        """
        处理浏览器请求
        :param self:
        :return:
        """
        # 接收客户端发送过来的数据
        recv_data = new_socket.recv(4096)
        # 如果没有收到数据，那么请求无效，关闭套接字，直接退出
        if len(recv_data) == 0:
            new_socket.close()
            return
        # 对接收的请求字节数据，转换成字符数据，进行解码
        request_data = recv_data.decode('utf-8')
        print("浏览器的请求数据：",request_data)
        request_array = request_data.split(' ', maxsplit=2) # maxsplit取前两个
        request_path = request_array[1] # 获取请求路径
        print('request_path:',request_path)
        if request_path == '/':
            request_path = '/index.html'

        # 根据请求路径判断是动态资源还是静态资源
        if request_path.endswith('.html'): # 以.html结尾
            """动态资源"""
            # 动态资源的请求交给web框架来处理，需要把请求参数传给web框架，可能会有多个参数
            params = {
                'request_path': request_path,
            }
            # web框架处理请求后，返回一个响应给客户端
            response = MyFramework.handle_request(params)
            new_socket.send(response)
            new_socket.close()

        else:
            """静态资源"""
            response_body = None
            response_header = None
            response_first_line = None # 响应头
            response_type = None # 响应头第一行
            # 请求静态资源就是根据请求路径读取/static目录中的静态文件数据，响应给客户端
            try:
                # 读取static目录中对应的文件数据，，rb模式是一种兼容模式，可以打开字节行文件
                with open('static'+request_path, 'rb', ) as f:
                    response_body = f.read()
                # 返回响应头（字符）
                if request_path.endswith(('.jpeg', 'webp')): # 判断请求的类型是否 jpeg和webp
                    response_type = 'image/webp'
                response_first_line = 'HTTP/1.1 200 OK\r\n'
                response_header = 'Content-Length: '+str(len(response_body))+'\r\n' \
                                  +'Content-Type: '+response_type+'; charset=UTF-8\r\n' \
                                  +'Date: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\r\n' \
                                  +'Server: MyServer\r\n'

            except Exception as e: # 客户端读取的文件不存在
                print('访问文件路径不存在：',e)
                with open('static/404.html', 'rb') as f:
                    response_body = f.read()  # 响应的主体页面（字节）
                # 返回响应头（字符）
                response_first_line = 'HTTP/1.1 404 Not Found\r\n'
                response_header = 'Content-Length: '+str(len(response_body))+'\r\n' \
                                  +'Content-Type: text/html; charset=UTF-8\r\n' \
                                  +'Date: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\r\n' \
                                  +'Server: MyServer\r\n'

            finally:
                # 组成响应数据，返回给客户端
                response = (response_first_line + response_header + '\r\n').encode('utf-8') + response_body
                new_socket.send(response)
                new_socket.close()


    def start(self):
        #循环多线程接受客户端的请求
        while True:
            new_socket, client_ip_post = self.socket_server.accept()
            print('客户端的ip和端口：',client_ip_post)
            # 一个客户端的请求交给一个线程处理
            sub_thread = threading.Thread(target=self.handle_browser_request, args=(new_socket,))
            sub_thread.setDaemon(True) # 设置当前线程为守护线程
            sub_thread.start() # 启动子线程


# web服务器程序的入口
def run_main():
    web_server = MyHttpWebServer(8080)
    web_server.start()

if __name__ == '__main__':
    run_main()
