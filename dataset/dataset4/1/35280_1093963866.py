from binascii import b2a_hex

class octetstring(str):
    def __repr__(self):
        return b2a_hex(str(self))
    def __str__(self):
        return b2a_hex(str(self))

o = octetstring('A')