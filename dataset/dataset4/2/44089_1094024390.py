from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
msg['From'] = '...@a.b'
msg['To'] = '...@x.y'
msg.epilogue = ''

msg.attach(MIMEText('aaaaaaaaaaaaaaaaaaaaaaaa'))