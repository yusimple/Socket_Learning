import socket
serverName, serverport = '', 8888
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # the AF_NET means address family,the SOCK_STREAM means HTTP
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
serverSocket.bind((serverName,serverport))
serverSocket.listen(1)
print(serverName,socket.AF_INET,":",serverport,"is servering for you")
while True:
    clientConnection, clientAddress = serverSocket.accept()
    request = clientConnection.recv(1024)
    print(request)
    http_response = clientAddress,"""\
HTTP/1.1 200 OK
    print("Hello World!")
"""
    clientConnection.sendall(bytes(http_response))
    clientConnection.close()
