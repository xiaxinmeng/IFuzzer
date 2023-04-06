from email.Charset import Charset,QP
from email.MIMEText import MIMEText

charset = Charset('utf-8')
charset.body_encoding = QP

msg = MIMEText(
    u'Some text with chars that need encoding: \xa3',
    'plain',
    )
# set the charset 
msg.set_charset(charset)