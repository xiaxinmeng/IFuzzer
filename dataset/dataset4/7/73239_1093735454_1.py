class MboxoFactory(mailbox.mboxMessage):
    def __init__(self, message=None):
        super().__init__(message=MboxoReader(message))