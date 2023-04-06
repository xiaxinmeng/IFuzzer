# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

msg = MIMEText("REAL_MSG_BODY_BEGIN\n...\nREAL_MSG_BODY_END")

msg['Subject'] = 'The contents of is this...'
msg['To'] = "TO toAddress@oststrom.com\r\nX-SPLIT-MSG-TO-BODY\r\n"
msg['From'] = "FROM fromAddress@oststrom.com"
msg['MyHEader'] = "hi :: hi"

print(msg)
print(repr(msg))
print("=========================")
import email
msg = email.message_from_string(str(msg))  
print(msg)

print("-> FROM: %s" % msg.get("From")) 
print("-> TO:   %s" % msg["To"]) 
print("-> MSG:  " + repr(msg.get_payload()))

