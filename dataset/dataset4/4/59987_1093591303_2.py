def f(a, b, prec=None):
    with localcontext() as c:
        c.prec = 9 if prec is None else prec
        return Decimal(a) / b