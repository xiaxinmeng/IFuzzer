for c in b'-!*+/' + ascii_letters.encode('ascii') + digits.encode('ascii'):
    _QUOPRI_HEADER_MAP[c] = chr(c)