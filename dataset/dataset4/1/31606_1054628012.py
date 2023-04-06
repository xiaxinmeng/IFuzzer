
def fRandom():
    mantissa = random.getrandbits(52)
    significand = 1.0 + mantissa * float_info.epsilon
    x = 0
    while not x:
        x = random.getrandbits(32)
        x = x & -x  # bitmask for rightmost 1-bit (exponential)
    return significand / (2 * x)

