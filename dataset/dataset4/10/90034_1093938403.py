def frac_sqrt(x: Fraction) -> float:
    'Return sqrt to greater precision than math.sqrt()'
    # Needed because a correctly rounded square root of
    # a correctly rounded input can still be off by 1 ulp.
    # Here we avoid the initial rounding and work directly
    # will the exact fractional input.  The square root
    # is first approximated with math.sqrt() and then
    # refined with a divide-and-average step. Since the
    # Newton-Raphson algorithm has quadratic convergence,
    # one refinement step gives excellent accuracy.
    a = Fraction(math.sqrt(x))
    return float((x / a + a) / 2)


def deci_sqrt(x: Fraction) -> float:
    ratio = Decimal(x.numerator) / Decimal(x.denominator)
    return float(ratio.sqrt())