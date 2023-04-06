def control(char):
    n = ord(char)
    if 0 <= n <= 0x1F:
        # C0 control codes
        return '^' + chr(ord('@')+n)
    elif n == 0x7F:
        # DEL
        return '^?'
    elif 0x80 <= n <= 0x9F:
        # C1 control codes
        return 'Esc+' + chr(ord('@')+n-0x80)
    else:
        raise ValueError('Not a control character.')