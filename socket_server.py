
'''在程序中，如果想要完成一个tcp服务器的功能，需要的流程如下：
socket创建一个套接字 socket(AF_INET,SOCK_STREAM)
bind绑定ip和port
listen使套接字变为可以被动链接
accept等待客户端的链接
recv/send接收发送数据'''

from socket import *
# 1、创建服务器套接字,设置重复使用绑定的信息
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 2、设置本机地址和端口
local_addr = ('127.0.0.1',8899)
# 3、绑定ip
server_socket.bind(local_addr)
# 4、设置最大连接数，开始监听tcp连接
server_socket.listen(100)
# 5、如果客户端有连接请求,必须使用accept来进行处理,
# accept返回两个参数，第一个是socket对象，第二个是连接方的地址
while True:
    print('---------------服务端等待连接的客户端----------------------')
    client_socket,client_addr = server_socket.accept() #这里会堵塞 只有客户端连接后 才往下走
    print('----------服务端已收到客户端消息正在处理----------')


    # 6、通过client_socket接收对方发送过来的数据
    recv_data = client_socket.recv(1024)
    # 7、打印接收到的数据
    print('接收到{}的数据为{}'.format(client_addr,recv_data.decode()))
    # 8、发送数据到客户端
    r_data = input('请回复内容:')
    client_socket.send(r_data.encode())
    # 9.关闭客户端服务套接字client_socket,
    # 只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
    client_socket.close()

