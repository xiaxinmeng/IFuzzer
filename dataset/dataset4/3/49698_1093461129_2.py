d1 = decimal.Decimal('999')
d2 = d1
context.prec = d1.precision + d2.precision
d3 = d1 * d2