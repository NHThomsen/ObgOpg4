from socket import *
import threading
import random

def handleClient(connectionSocket, addr):
    while True:
        recieved = connectionSocket.recv(1024).decode()
        case = recieved.split(',')[0]
        firstNumber = int(recieved.split(',')[1])
        secondNumber = int(recieved.split(',')[2])
        sendResult = ""
        if case == 'Random':
            sendResult = random.randint(firstNumber,secondNumber)
        elif case == "Add":
            sendResult = firstNumber + secondNumber
        elif case == "Subtract":
            sendResult = firstNumber - secondNumber
        connectionSocket.send(str(sendResult).encode())

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient,args=(connectionSocket,addr)).start()