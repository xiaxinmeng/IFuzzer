from decimal import Context

context = Context(prec=2)

for x in [100., 10., 1., 0.1]:
    print(context.create_decimal_from_float(x), context.create_decimal_from_float(4.56*x))