if 1:
    class Bytes(bytes):
        def __new__(cls, name, encoding='ascii'):
            return bytes.__new__(cls, name.encode())
        __repr__ = bytes.decode
    print(repr(Bytes("LOAD_NAME")))