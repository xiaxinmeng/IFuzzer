import email.message

msg = email.message.EmailMessage()
msg.set_payload('Hello World\n')
msg.set_unixfrom('From foo@bar Thu Jan  1 00:00:00 1970')
msg['Subject'] = 'Hello'
msg['From'] = 'Me <me@foo.bar>'
print('as_string:')
print(msg.as_string(unixfrom=True))
print('as_bytes:')
print(msg.as_bytes(unixfrom=True).decode())