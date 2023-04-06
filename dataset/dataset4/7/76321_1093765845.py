from fractions import Fraction
U=Fraction(1)

def test(x):
    for i in range(1, x.denominator):
        x*=x
        yield i, i*x

for m, n in test(U*3/5):
    print (m, n)