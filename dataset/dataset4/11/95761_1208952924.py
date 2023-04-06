class CancelledErrorGroup(BaseExceptionGroup, CancelledError):
    """A group of errors containing a CancelledError."""

    # This error type needed for "backwards compatibility" with code that
    # has `except CancelledError: ...; raise`-style blocks.

    def derive(self, excs):
        et = BaseExceptionGroup
        if any(e for e in excs if isinstance(e, CancelledError)):
            et = CancelledErrorGroup
        return et(self.message, excs)
