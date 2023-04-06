s = Summer() # new object
s.add(3.1)   # add one number to running sum
s.sum()      # returns sum so far as float: 3.1
s.update(iterable_returning_numbers)  # add a bunch of numbers to sum
s.combine(another_Summer_object)  # add Summer's
s.sum_as_decimal(precision=None) # sum so far as Decimal
s.sum_as_fraction()  # exact sum so far as Fraction