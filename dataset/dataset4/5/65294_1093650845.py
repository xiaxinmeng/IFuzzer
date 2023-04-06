import email.message, email.header
m = email.message.Message()
m['Subject'] = email.header.Header('Böðvarr'.encode('latin-1'), 'latin-1')
print(m.as_string())