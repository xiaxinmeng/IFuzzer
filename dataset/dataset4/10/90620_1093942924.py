
from email import message_from_bytes
from email.policy import SMTPUTF8

eml_bytes = b'Header-With-FS-Char: BEFORE\x1cAFTER\r\n\r\nBody\r\n'
print(eml_bytes)

message = message_from_bytes(eml_bytes, policy=SMTPUTF8)
print(message.as_bytes(policy=SMTPUTF8))
