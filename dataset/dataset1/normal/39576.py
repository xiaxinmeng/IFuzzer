import decimal
c = decimal.getcontext()
c.prec = decimal.MAX_PREC
i = decimal.Decimal(4)
i / 2
