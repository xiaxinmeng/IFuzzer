import smtplib
from email.message import Message
import datetime
import sys

msg= Message()
msg.set_charset('latin-1')
msg['Subject'] = "*** Email Test ***"