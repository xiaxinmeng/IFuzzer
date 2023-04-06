import socket, threading, time

fd_0 = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
fd_0.bind    (('localhost', 8000))
fd_0.connect (('localhost', 8001))

fd_1 = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
fd_1.bind    (('localhost', 8001))
fd_1.connect (('localhost', 8000))

def thread_main ():
  for i in range (3) :
    # print ('recvfrom  blocking ...')                                          
    recv, remote_addr = fd_0.recvfrom (1024)
    print ('recvfrom  %s  %s' % (recv, remote_addr))

def main ():
  fd_1.send (b'test')
  fd_1.send (b'')
  fd_0.shutdown (socket.SHUT_RD)

thread = threading.Thread ( target = thread_main )
thread.start ()
time.sleep (0.5)
main ()
thread.join ()
print ('exiting')