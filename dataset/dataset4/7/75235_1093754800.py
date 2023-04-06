import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

body = "this is a test"

#craft the message
fromaddr = 'ned@example.com'
server = smtplib.SMTP('smtp.example.com', 587)
p = 'Hunter2!'
subject = "test"
toaddr = "foo@example.com"
ccaddr = "bar@example.com"
bccaddr = "baz@example.com"

msg = MIMEMultipart()