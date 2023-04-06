def mk_full_coeff(x):
    prec = getcontext().prec
    adj = x.adjusted()
    if adj >= prec:
        return +x
    else:
        return x.quantize(Decimal(1).scaleb(adj-prec+1))