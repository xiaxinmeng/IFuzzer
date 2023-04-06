from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('',9999))
ss = ssl(s,None,None)
ss.write("foo!\n")