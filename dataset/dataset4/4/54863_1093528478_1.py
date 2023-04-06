from datetime import datetime

class SubclassDatetime(datetime):
    sub_var = 1

a = SubclassDatetime(2002, 3, 2, 17, 6)
# Add/sub ints or floats should be illegal
for i in 1, 1.0:
    a+i