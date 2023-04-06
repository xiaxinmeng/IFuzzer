smtp = smtplib.SMTP(host, port=25)
smtp.ehlo()
smtp.sendmail(from_mail, to_mail, data)