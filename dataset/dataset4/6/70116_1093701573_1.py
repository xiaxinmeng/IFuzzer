import timeit

old_setup = """
import random
from decimal import Decimal

def _decimal_to_ratio(d):
    sign, digits, exp = d.as_tuple()
    if exp in ('F', 'n', 'N'):  # INF, NAN, sNAN
        assert not d.is_finite()
        return (d, None)
    num = 0
    for digit in digits:
        num = num*10 + digit
    if exp < 0:
        den = 10**-exp
    else:
        num *= 10**exp
        den = 1
    if sign:
        num = -num
    return (num, den)

def run_it():
    dec = Decimal(str(random.random()))
    _decimal_to_ratio(dec)
"""

new_setup = """
import random
from decimal import Decimal

def _decimal_to_ratio(d):
    sign, exp = d._sign, d._exp
    if exp in ('F', 'n', 'N'):  # INF, NAN, sNAN
        assert not d.is_finite()
        return (d, None)
    num = int(d._int)
    if exp < 0:
        den = 10**-exp
    else:
        num *= 10**exp
        den = 1
    if sign:
        num = -num
    return (num, den)

def run_it():
    dec = Decimal(str(random.random()))
    _decimal_to_ratio(dec)
"""

if __name__ == '__main__':
    print("Testing proposed implementation")
    print("number = 10000")
    print(timeit.Timer(stmt='run_it()', setup=new_setup).timeit(number=10000))
    print("number = 100000")         
    print(timeit.Timer(stmt='run_it()', setup=new_setup).timeit(number=100000))
    print("number = 1000000")     
    print(timeit.Timer(stmt='run_it()', setup=new_setup).timeit(number=1000000))

    print("Testing old implementation")
    print("number = 10000")
    print(timeit.Timer(stmt='run_it()', setup=old_setup).timeit(number=10000))
    print("number = 100000")         
    print(timeit.Timer(stmt='run_it()', setup=old_setup).timeit(number=100000))
    print("number = 1000000")     
    print(timeit.Timer(stmt='run_it()', setup=old_setup).timeit(number=1000000))