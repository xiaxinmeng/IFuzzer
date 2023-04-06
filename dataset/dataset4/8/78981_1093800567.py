from email.message import EmailMessage
from email.policy import default
msg=EmailMessage(default.clone(max_line_length=None)) # or max_line_length=0

msg.set_content('あ') # raise error
# or
msg.set_content(b'a',maintype='application',subtype='octet-stream') # raise error