from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 4242))
mreq = inet_aton('224.0.0.1') + inet_aton('127.0.0.1')
s.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
s.recv(100)