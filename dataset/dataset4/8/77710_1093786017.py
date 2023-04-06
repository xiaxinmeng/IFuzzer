import email.header
import email.message

msg = email.message.Message()
msg.set_charset("UTF-8")
msg['Subject'] = email.header.Header(u'\u0105' * 12, maxlinelen=20, charset="UTF-8")
print(msg.as_string())