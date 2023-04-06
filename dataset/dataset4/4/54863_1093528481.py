from _datetime import date, datetime

class SubclassDate(date):
    sub_var = 1

a = SubclassDate(2002, 3, 2)
for i in 1, 1.0:
    print(a+i)  # "NotImplemented"

class SubclassDateTime(datetime):
    sub_var = 1

a = SubclassDateTime(2002, 3, 2, 3, 5)
for i in 1, 1.0:
    print(a+i)  # "NotImplemented"
a-i # TypeError: unsupported operand type(s) for -: 'SubclassDateTime' and 'float'