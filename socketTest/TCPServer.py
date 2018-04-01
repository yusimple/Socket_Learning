from socket import *
serverPort = 1997
serverName = "yusimple"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.decode().upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()