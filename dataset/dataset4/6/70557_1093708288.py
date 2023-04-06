def basestringencode(s, encoding=sys.getdefaultencoding(), errors="strict"):
    if isinstance(s, str):
        # Decode with provided rules, so a str with illegal characters
        # raises exception, replaces, ignores, etc. per arguments
        s = s.decode(encoding, errors)
    return s.encode(encoding, errors)