if __debug__:
    if not value.conditional():
        raise AssertionError(expression, value, conditional)