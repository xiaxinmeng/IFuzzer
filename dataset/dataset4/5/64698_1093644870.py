from statistics import variance as v
from statistics_with_exact_ratios import variance as v2
from fractions import Fraction

data = [Fraction(1,x) for x in range(1,2000)]

print('calculating variance using original statistics module ...')
print(float(v(data)))
print('now using exact ratio calculations ...')
print(float(v2(data)))