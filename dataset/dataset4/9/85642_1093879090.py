
import smtplib

smtp = smtplib.SMTP()
smtp.connect('smtp.gmail.com')
smtp.ehlo_or_helo_if_needed()
smtp.close()
try:
    smtp.quit()
except smtplib.SMTPServerDisconnected:
    pass
smtp.connect('smtp.gmail.com')
print(smtp.mail('user@example.com'))
