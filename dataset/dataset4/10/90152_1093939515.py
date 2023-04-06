
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = 'from@example.com'
msg['To'] = 'to@example.com'
msg['Subject'] = 'Subject'

msg.add_alternative('Hello, world.', subtype='text')
msg.add_alternative('<h1>Helo, world.</h1>', subtype='html')
with open('example.pdf', 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='pdf',
        filename='example.pdf'
    )

with smtplib.SMTP('SMTP_HOST', 'SMTP_PORT') as smtp:
    smtp.starttls()
    smtp.login('USER', 'PASSWORD')
    smtp.send_message(msg)
