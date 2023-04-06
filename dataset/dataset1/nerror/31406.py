import decimal
import fractions

class BadRational(fractions.Fraction):
    numerator = None
    denominator = 42

decimal.Decimal() < BadRational()
