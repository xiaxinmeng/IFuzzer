def decimalbase_digits2(x):
    bits = x.bit_length()
    return 1 + bits // (3 * _PyLong_DECIMAL_SHIFT)