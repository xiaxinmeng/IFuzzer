#coding: utf-8
import email.utils
from email.message import EmailMessage
from smtplib import SMTP
m = EmailMessage()
m['From'] = email.utils.formataddr(("Michaël", "michael@example.com"))
m['To'] = email.utils.formataddr(("René", "bounce@rodacom.fr"))
with SMTP('localhost') as smtp:
    smtp.set_debuglevel(2)
    smtp.send_message(m)
#END