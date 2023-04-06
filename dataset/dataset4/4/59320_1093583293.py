from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

msg = MIMEMultipart()
msg['Subject'] = 'Bug test'

text_part = MIMEText('actual content doesnt matter')
text_part.set_charset('utf-8')
msg.attach(text_part)

xml_part = MIMEText(b'<xml>aaa</xml>')
xml_part.set_type('text/xml')
xml_part.set_charset('utf-8')
encoders.encode_base64(xml_part)
msg.attach(xml_part)

print(msg.as_string())