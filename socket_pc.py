import socket
# 第一步：创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 第二步：连接服务端
sock.connect(('127.0.0.1', 8899))
# 第三步:给服务端发请求
data = '你好服务端，我是sq'.encode()
sock.send(data)
# 第四步:获取服务端返回的数据
res = sock.recv(1024)
print('服务端返回的数据:{}'.format(res.decode()))
# 关闭套接字
res.decode()


import unittestreport