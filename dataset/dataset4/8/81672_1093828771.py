# bpo_37491.py
from email.parser import BytesParser, Parser
from email.policy import default

payload = 'Content-Type:"'
msg = Parser(policy=default).parsestr(payload)
print(msg.get('content-type'))