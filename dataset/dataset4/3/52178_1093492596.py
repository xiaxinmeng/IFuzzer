_re_stripid = re.compile(r' at 0x[0-9a-f]{6,16}(>+)$', re.IGNORECASE)
def stripid(text):
    """Remove the hexadecimal id from a Python object representation."""
    # The behaviour of %p is implementation-dependent in terms of case.
    if _re_stripid.search(repr(Exception)):
        return _re_stripid.sub(r'\1', text)
    return text