def hangulsyllabledecomposition(c):
    if not 0xAC00 <= ord(c) <= 0xD7A3 : raise ValueError('only Hangul syllables allowed')
    dLV, T = divmod(ord(c) - 0xAC00, 28)
    if T!=0 : #it is a LVT syllable, decomposed into LV:=dLV*19 and T 
        return f'{0xAC00+dLV*28:04X} {0x11A7+T:04X}'
    else : #it is a LVT syllable, decomposed into L , V
        L, V = divmod(dLV,21)
        return f'{0x1100+L:04X} {0x1161+V:04X}'
    # Constants used:
    # 