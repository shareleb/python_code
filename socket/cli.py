from socket import *

HOST = '172.17.255.222'
PORT = 21000
BUFSIZ =1024
ADDR=(HOST,PORT)
cli = socket(AF_INET,SOCK_STREAM)
cli.connect(ADDR)


while True:
    data = input('input:')
    if data == 'finish':
        print("break connect...")
        data = data.encode('utf-8')
        cli.send(data)
        break
    else:
        data = data.encode('utf-8')
        cli.send(data)
        data=cli.recv(BUFSIZ)
        data = data.decode('utf-8')
        print("server:{}".format(data))


cli.close()


