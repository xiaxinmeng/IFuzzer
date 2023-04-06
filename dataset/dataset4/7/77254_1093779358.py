def as_integer_ration(x):
    if hasattr(x, 'as_integer_ration'):
        return x.as_integer_ration()
    else:
        return (x.numerator, x.denominator)