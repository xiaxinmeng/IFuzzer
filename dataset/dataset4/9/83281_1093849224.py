from email import message_from_binary_file
from email.policy import SMTP

msg = message_from_binary_file(open('mail.eml', 'rb'), policy=SMTP)
print(msg)