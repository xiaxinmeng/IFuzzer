class Mailbox(mailbox.PortableUnixMailbox):
    def __init__(self, fp):
        mailbox.PortableUnixMailbox.__init__(self, fp,
email.message_from_file)