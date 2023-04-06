import smtplib
from email.message import EmailMessage
from email.utils import formataddr

server = smtplib.SMTP('smtp.xxx.com',port=25)
server.login('you@xxx.com', 'password')
msg = EmailMessage()