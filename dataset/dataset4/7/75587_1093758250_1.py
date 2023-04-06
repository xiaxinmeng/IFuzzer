import decimal
import fractions

class BadRational(fractions.Fraction):
    numerator = 42
    denominator = None