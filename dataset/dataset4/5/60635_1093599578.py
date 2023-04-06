import decimal

class MyDecimal(decimal.Decimal):
    def __new__(cls, value):
        return super().__new__(cls, value)

a = decimal.Decimal('1.0')
b = MyDecimal(a)
c = MyDecimal('1.0')