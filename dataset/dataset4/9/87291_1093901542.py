import smtplib, ssl
port = 587  
smtp_server = "---------------"
smtpserver = smtplib.SMTP(smtp_server, port)
smtpserver.set_debuglevel(2)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login("", "")