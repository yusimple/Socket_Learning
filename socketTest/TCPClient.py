from socket import *
serverName = 'yusimple'
serverPort = 1997
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("please input a sentence")
sentence = input()
clientSocket.send(sentence.encode())
modifiedMessage=clientSocket.recv(1024).decode()
print('From the Server:',modifiedMessage)
clientSocket.close()