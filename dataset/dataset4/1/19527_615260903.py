def randbytes(gen, n):
    return gen.getrandbits(n * 8).to_bytes(n, 'little')