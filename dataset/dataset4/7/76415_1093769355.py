class Mailbox(MMDF):
    """A mailbox that interoperates with the 'with' statement."""

    def __enter__(self):
        self.lock()
        return self

    def __exit__(self, *exc):
        self.flush()
        self.unlock()
        # Don't suppress the exception.
        return False