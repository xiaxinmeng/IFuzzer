def decimalbase_digits1(x):
    bits = size(x) * PyLong_SHIFT
    return 1 + bits // (3 * _PyLong_DECIMAL_SHIFT)