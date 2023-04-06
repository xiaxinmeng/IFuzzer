from email.mime.text import MIMEText
msg = MIMEText('<div/>', 'html')
msg["To"] = "this.email.shouldnt.be.printed@nokia.com"
msg["To"] = "valid.email@nokia.com"
print(msg["To"])