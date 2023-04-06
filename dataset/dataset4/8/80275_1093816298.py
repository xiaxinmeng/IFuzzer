
import smtplib


smtp_server = "smtp.163.com"
con2 = smtplib.SMTP_SSL()
con2.connect(smtp_server, 465)
