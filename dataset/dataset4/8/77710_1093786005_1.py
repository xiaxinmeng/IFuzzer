from email.message import EmailMessage
from email.policy import default

policy = default # max_line_length = 78
msg = EmailMessage()
msg["Subject"] = "á"*100
policy.fold("Subject", msg["Subject"])