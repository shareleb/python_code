from socket import *
from time import ctime 

HOST = '172.17.255.222'
PORT = 21000
BUFSIZ = 1024

ADDR= (HOST,PORT)
server= socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)


while True:
    print('waiting for connection...')
    temp,addr = server.accept()
    print ('...connnected from:',addr)

    while True:
        data = temp.recv(BUFSIZ)
        data = data.decode('utf-8') 
        if data == "finish":
            print("break connection...")
            break
        else:
            print("client say>",data)
            temp.send(ctime().encode('utf-8'))
        
    temp.close()
server.close()




