
if amt is not None:
    # Amount is given, implement using readinto
    b = bytearray(amt)
    n = self.readinto(b)
    return memoryview(b)[:n].tobytes()
