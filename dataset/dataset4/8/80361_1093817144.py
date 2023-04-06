
import mailbox

mbox = mailbox.mbox("broken.mbox")
for msg in mbox:
    msg.get_payload()
