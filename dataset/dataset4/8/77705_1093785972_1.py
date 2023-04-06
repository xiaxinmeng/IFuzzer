from email.message import EmailMessage
from email.policy import default

policy = default.clone(max_line_length=0)
msg = EmailMessage()
msg["Subject"] = "á"
policy.fold("Subject", msg["Subject"])