from email.header import Header
m = MIMEText('foo')
m['subject']=Header('something long')