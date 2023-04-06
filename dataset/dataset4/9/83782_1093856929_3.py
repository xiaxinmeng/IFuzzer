
class Decimal:
    def __init__(self, value):
        pass
    def __format__(self, template):
        return template
width = 10
precision = 4
value = Decimal('12.34567')
print("Expect Template to be '10.4' (TRUE)")
print(f'result0: {value:{width}.{precision}}')
print("Expect Template to be 'width.precision' (TRUE)")
print(f'result1: {value:width.precision}')
print("Expect Template to be '{width}.{precision}' (FALSE)")
print(f'result2: {value:{{width}}.{{precision}}}') # ACTUAL: {10}.{4}
