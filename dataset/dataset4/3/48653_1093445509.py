import smtplib
import email.mime.text

msg = email.mime.text.MIMEText("Ümlaut", _charset="UTF-8")

smtp = smtplib.SMTP('localhost')
smtp.sendmail('gus@flyingmeat.com', 'gus@flyingmeat.com', "Subject: This is your mail\n" + msg.as_string())
smtp.quit()