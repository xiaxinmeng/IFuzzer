import socket

host = "xx.xx.xx.xx"
port = xxxx
DSN  = "xxxx;UID=xxxx;"
length = 1024

Request = '''xxxxxxx'''

socket = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
socket.connect((host,port))