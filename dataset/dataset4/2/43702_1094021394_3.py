#python 2.5
from email.MIMEText import MIMEText
m = MIMEText(None, 'html', 'iso-8859-1')
m.set_payload(m._charset.body_encode('abc' * 50))