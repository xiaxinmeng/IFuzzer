num = self.numerator
den = self.denominator
while not (isinstance(num, Integral) and isinstance(den, Integral)):
    num = num.numerator * den.denominator
    den = den.numerator * num.denominator
return float(int(num) / int(den))