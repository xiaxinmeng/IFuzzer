
import decimal
import tracemalloc
tracemalloc.start()
if 0:
    ctx = decimal.getcontext()
    ctx.prec = decimal.MAX_PREC
    ctx.Emax = decimal.MAX_EMAX
    ctx.Emin = decimal.MIN_EMIN
num = decimal.Decimal(1) / decimal.Decimal(7)
mem = tracemalloc.get_traced_memory()[1]
print("Peak memory usage: %.1f kB" % mem)
