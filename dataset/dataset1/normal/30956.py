import socket
from ftplib import FTP
try:
    ftp = FTP('host.i.know.will.hang.com', timeout=1)
except socket.timeout:
    print('caught')
