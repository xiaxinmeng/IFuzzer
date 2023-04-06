server = smtplib.SMTP('localhost')
server.sendmail(mailfrom, rcptto, msg)
server.quit()