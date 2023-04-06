with open("test.mbox",'w') as f:
    f.write("From sender@invalid Thu Nov 17 00:49:30 2016\n")
    f.write("Subject: Test\n")
    f.write("\n")
    f.write("\n")

import mailbox
messages = mailbox.mbox("test.mbox")
for msg in messages:
    print(msg.get('subject'))
    print(msg.get_from())
    print(msg.get_unixfrom())