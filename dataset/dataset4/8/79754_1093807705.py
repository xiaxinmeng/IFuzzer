IPV4_RE = re.compile(r"\.\d+$", re.ASCII)
def is_HDN(text):
    """Return True if text is a host domain name."""
    # XXX
    # This may well be wrong.  Which RFC is HDN defined in, if any (for
    #  the purposes of RFC 2965)?
    # For the current implementation, what about IPv6?  Remember to look
    #  at other uses of IPV4_RE also, if change this.
    if IPV4_RE.search(text):
        return False
    if text == "":
        return False
    if text[0] == "." or text[-1] == ".":
        return False
    return True