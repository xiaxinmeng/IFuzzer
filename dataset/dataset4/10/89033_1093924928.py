from io import BytesIO
from os import read
import email

fp = BytesIO()

with open('mail.eml', 'rb') as f:
    filecontent = f.read()
    print("type(filecontent)= ", type(filecontent))
    fp.write(filecontent)

mailobj = email.message_from_bytes(fp)