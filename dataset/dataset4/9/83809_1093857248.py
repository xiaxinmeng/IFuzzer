
msg = email.message_from_bytes(...)
for part in msg.walk():
  content_type = part.get_content_type()
  if not part.get_content_maintype() == 'multipart':
     filename = part.get_filename(None)
     attachment = part.get_payload(decode=True)
