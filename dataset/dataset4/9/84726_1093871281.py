if offset is not None:
    caretspace = badline.rstrip('\n')
    offset = min(len(caretspace), offset) - 1
    caretspace = caretspace[:offset].lstrip()
    # non-space whitespace (likes tabs) must be kept for alignment
    caretspace = ((c.isspace() and c or ' ') for c in caretspace)
    yield '    {}^\n'.format(''.join(caretspace))