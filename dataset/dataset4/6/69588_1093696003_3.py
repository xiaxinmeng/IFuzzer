def decimalbase_digits4(x):
    bits = size(x) * PyLong_SHIFT
    return bits * 10000 // (33219 * _PyLong_DECIMAL_SHIFT)