
def body_encode(s, maxlinelen=76, eol=NL):
    r"""Encode a string with base64.

    Each line will be wrapped at, at most, maxlinelen characters (defaults to
    76 characters).

    Each line of encoded text will end with eol, which defaults to "\n".  Set
    this to "\r\n" if you will be using the result of this function directly
    in an email.
    """
    if not s:
        return s
