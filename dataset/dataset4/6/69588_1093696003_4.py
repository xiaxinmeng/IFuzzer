def new_decimalbase_digits5(x):
    bits = x.bit_length()
    return bits * 10000 // (33219 * _PyLong_DECIMAL_SHIFT)