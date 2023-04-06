from decimal import Context

def dec(num, prec):
    return Context(prec=prec).create_decimal('{{:.{:d}e}}'.format(prec - 1).format(num))