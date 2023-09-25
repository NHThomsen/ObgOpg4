from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket  = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    print('Pick Either: Random, Add or Subtract: ')
    case = input()
    while case != 'Random' and case != 'Add' and case != 'Subtract':
        print('Pick Either: Random, Add or Subtract: ')
        case = input()

    orderImportant = True
    
    while orderImportant:
        print('Pick first number: ')
        firstNumber = int(input())
    
        print('Pick second number: ')
        secondNumber = int(input())
    
        if secondNumber > firstNumber and case == 'Random':
            orderImportant = False
        elif secondNumber < firstNumber and case == 'Random':
            print('Second number must be greater than first number')
    
        if case == 'Add':
            orderImportant = False
        
        if firstNumber > secondNumber and case == 'Subtract':
            orderImportant = False
        elif firstNumber < secondNumber and case == 'Subtract':
            print('First number must be greater than second number')


    sendString = str(case+','+str(firstNumber)+','+str(secondNumber)).encode()
    clientSocket.send(sendString)
    recievedResult = clientSocket.recv(1024).decode()
    print(recievedResult)