def deprecation(message):
    warnings.warn(message, DeprecationWarning, 2)