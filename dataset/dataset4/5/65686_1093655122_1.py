def _count_righthand_zero_bits(number, bits):
    if not number:
        return bits
    return (~(number | -number)).bit_length()