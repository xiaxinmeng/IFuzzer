def serialize(value: int, signed=True) -> bytes:
    x = value.to_bytes(-1, 'big', signed=signed)
    l = len(x).to_bytes(4, 'big', signed=False)
    return l + x