def check(exponent):
    factor = 10**exponent
    for x in range(5, 5+20000, 20):
        if not round(float(x*factor), -1-exponent) < x*factor:
            yield float(x*factor)