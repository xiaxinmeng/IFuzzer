import smtplib
server = "localhost"
sendit = smtplib.SMTP(server)
sendit.set_debuglevel(1)
sendit.sendmail("ser", "ser, ser, ser, ser", "dupa")
sendit.quit()