def decimalbase_digits3(x):
    digits = size(x)
    d = (33 * _PyLong_DECIMAL_SHIFT) // (10 * PyLong_SHIFT - 33 * _PyLong_DECIMAL_SHIFT)
    return 1 + digits + digits // d