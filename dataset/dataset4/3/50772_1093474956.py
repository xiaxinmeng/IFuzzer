import smtplib
smtp = smtplib.SMTP()
smtp.connect('mail.myserver.org')
smtp.login('myusername', 'mypassword')