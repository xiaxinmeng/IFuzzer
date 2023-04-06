import datetime

x = [datetime.timedelta(1), datetime.timedelta(2)]
print(x[0] + x[1])  # datetime.timedelta(3)
print(sum(x))  # TypeError: unsupported operand type(s) for +: 'int' and 'datetime.timedelta'