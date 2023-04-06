
# coding:utf-8
from socket import *
from multiprocessing import *
from time import sleep

def dealWithClient(newSocket,destAddr):
    recvData = newSocket.recv(1024)
    newSocket.send(b"""HTTP/1.1 100 OK\n""")

    while True:
        # recvData = newSocket.recv(1024)
        newSocket.send(b"""x:a\n""")

        if len(recvData)>0:
            # print('recv[%s]:%s'%(str(destAddr), recvData))
            pass
        else:
            print('[%s]close'%str(destAddr))
            sleep(10)
            print('over')
            break

    # newSocket.close()


def main():

    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
    localAddr = ('', 8085)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            newSocket,destAddr = serSocket.accept()

            client = Process(target=dealWithClient, args=(newSocket,destAddr))
            client.start()

            newSocket.close()
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()
