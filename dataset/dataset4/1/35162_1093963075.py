infile = open("test.mbox")
for msg in mailbox.PortableUnixMailbox(infile):
    pass