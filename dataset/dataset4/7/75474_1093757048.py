class BadFloat(float):
    def as_integer_ratio(self):
        return 1 << 1000

decimal.Decimal.from_float(BadFloat())