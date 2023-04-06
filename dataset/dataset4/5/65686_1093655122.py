def _count_righthand_zero_bits(number, bits):
    if not number:
        return bits
    return (~number & (number-1)).bit_length()