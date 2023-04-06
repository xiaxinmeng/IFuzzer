import sys
import mailbox
from email.message import EmailMessage
from email.headerregistry import Address
from email import policy

ePol = policy.SMTP.clone(refold_source='long',max_line_length=78)
msg = EmailMessage(ePol)
msg['From'] = Address("abcdefgh ijklnopq","a.ijklnopq","antani.com")
msg['To'] = (Address("abcdef.ghijklmno@pqrstuvwxyz12345678.it","abcdef.ghijklmnop","pqrstuvwxyz12345678.it"), Address("Jane Doe", "jane", "doe.com"))
msg['Subject'] = "Test"
msg.set_content("Body")
finalMail = msg.as_string()