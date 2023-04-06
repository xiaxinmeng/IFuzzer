#########################################"
from email.mime.text import MIMEText

msg = MIMEText("""Hello World""")

dest = ["one@example.com", "two@example.com", "three@example.com", "four@example.com"]
 
for d in dest:
    msg["From"] = "myself@example.com"
    msg["To"] = d
    msg["subject"] = "just a test"
    print (msg)
    # + send the buggy mail...
###################################