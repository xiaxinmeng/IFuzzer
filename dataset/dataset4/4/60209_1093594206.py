smtp = smtplib.SMTP(host, port=25)
smtp.ehlo()
try:
    smtp.sendmail(from_mail, to_mail, data)
except Exception as e:
    print(e)

smtp.quit()