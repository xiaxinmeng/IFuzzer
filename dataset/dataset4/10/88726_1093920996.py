from email.message import EmailMessage

m = EmailMessage()
m['Subject'] = '中文'

print(bytes(m))