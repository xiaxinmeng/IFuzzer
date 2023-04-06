from decimal import *

for i in range(1000):
    with localcontext() as c:
        c.prec = 2
        with localcontext() as x:
            x.prec = 4
            Decimal(10) / 3
        Decimal(10) / 3

