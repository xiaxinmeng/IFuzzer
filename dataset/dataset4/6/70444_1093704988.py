from decimal import *

c = getcontext()
c.prec = MAX_PREC
c.Emax = MAX_EMAX
c.Emin = MIN_EMIN

x = Decimal(2)**74207281 - 1
s = str(x)
assert s[:12] == "300376418084"
assert s[-12:] == "391086436351"