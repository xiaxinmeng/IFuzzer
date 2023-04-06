import socket, threading, time

sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
sock.bind (('localhost', 8000))

def recvfrom ():
  for i in range (2) :
    print ('recvfrom  blocking ...')
    recv, remote_addr = sock.recvfrom (1024)
    print ('recvfrom  %s  %s' % (recv, remote_addr))

thread = threading.Thread ( target = recvfrom )
thread.start ()
time.sleep (0.5)

sock2 = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
sock2.sendto (b'test', ('localhost', 8000))