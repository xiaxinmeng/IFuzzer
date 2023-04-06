
class Message(email.message.Message):

    def as_string(self):
        # Work around for https://bugs.python.org/issue27321 and
        # https://bugs.python.org/issue32330.
        try:
            value = email.message.Message.as_string(self)
        except (KeyError, LookupError, UnicodeEncodeError):
            value = email.message.Message.as_bytes(self).decode(
                'ascii', 'replace')
        # Also ensure no unicode surrogates in the returned string.
        return email.utils._sanitize(value)
