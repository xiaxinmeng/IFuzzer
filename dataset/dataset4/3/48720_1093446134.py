import smtplib

s = smtplib.SMTP_SSL("relay-auth.rwth-aachen.de")
s.login("***", "***")
s.sendmail("bronger@physik.rwth-aachen.de", ["bronger.randys@googlemail.com"], "Hello")