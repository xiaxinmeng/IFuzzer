import decimal
class MyDecimal(decimal.Decimal):
    x = None
    def __new__(cls, value):
        return super().__new__(cls, value)
        return obj
a = MyDecimal("1.1")
a.x = 3
b = MyDecimal(a)
print(a.x, b.x)