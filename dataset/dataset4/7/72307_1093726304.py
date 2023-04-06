from blaze.expr import symbol
from blaze.interactive import data
from blaze.compute import compute

t = symbol('t', 'var * {amount: int64, id: int64, name: string}')

sql = data('sqlite:///:memory:::accounts', dshape=t.dshape)

expr = t.distinct().nrows
x = expr._subs({t: sql})
result = compute(x)