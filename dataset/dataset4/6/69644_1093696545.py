import ftplib
import socket
import re


ftp = ftplib.FTP()
ftp.set_debuglevel(1)
ftp.connect('ftp.debian.org', timeout=10)
ftp.login('anonymous','user@example.com')
ftp.sendcmd('TYPE A')

s = ftp.transfercmd('LIST')