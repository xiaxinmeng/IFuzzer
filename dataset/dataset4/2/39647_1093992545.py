from socket import *
from select import select
s = [socket(AF_INET, SOCK_DGRAM) for i in range(512)]
select(s, [], [], 1)