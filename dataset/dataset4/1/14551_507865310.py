
from email.parser import BytesParser, Parser
from email.policy import default


payload = 'Content-Type:x;\x1b*="\'G\'\\"g'
msg = Parser(policy=default).parsestr(payload)
