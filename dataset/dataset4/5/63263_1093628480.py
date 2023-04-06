from email.mime.nonmultipart import *
from email.charset import *
from email.message import Message
from io import BytesIO
from email.generator import BytesGenerator
msg = Message()
cs = Charset('utf-8')
cs.body_encoding = None
msg.set_payload('АБВ', cs)
msg.as_string()
fp = BytesIO()
g = BytesGenerator(fp)
g.flatten(msg)
print(fp.getvalue())