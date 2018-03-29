from socket import *
serverName = 'yusimple'
serverPort = 1997
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input()
clientSocket.send(sentence)
modifiedMessage=-clientSocket.rec(1024)
print('From the Server:',modifiedMessage)
clientSocket.close()