from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(IPPROTO_IP, IP_MULTICAST_IF, inet_aton('127.0.0.1'))
s.sendto(b'foo', ('224.0.0.1', 4242))