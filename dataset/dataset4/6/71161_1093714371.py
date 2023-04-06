from decimal import Decimal
class BadFloat(float):
    def as_integer_ratio(self):
        return 1
    def __abs__(self):
        return self

Decimal.from_float(BadFloat(1.2))