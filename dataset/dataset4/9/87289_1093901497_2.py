# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

msg = MIMEText("REAL_MSG_BODY_BEGIN\n...\nREAL_MSG_BODY_END")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of is this...'
msg['To'] = "TO toAddress@oststrom.com"
msg['From'] = "FROM fromAddress@oststrom.com"
msg['MyHEader'] = "hi :: hi"
msg["m\r\nh"] = "yo"

print(msg)
print(repr(msg))
print("=========================")
import email
msg = email.message_from_string(str(msg))  
msg.add_header("CUSTOM-HEADER: yo\r\n\nX-INJECTED: injected-header\r\naa","data")
print(msg)

print("-> FROM: %s" % msg.get("From")) 
print("-> TO:   %s" % msg["To"]) 
print("-> MSG:  " + repr(msg.get_payload()))

