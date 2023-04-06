import smtplib
s = smtplib.SMTP("localhost")
s.sock.settimeout(5)
s.starttls()
s.helo("localhost")