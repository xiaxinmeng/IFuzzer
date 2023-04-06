class Rational(Real):
    ...
    def as_integer_ratio(self):
        return (self.numerator, self.denominator)