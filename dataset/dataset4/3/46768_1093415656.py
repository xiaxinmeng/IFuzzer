pycon
"""
It would be *much* more useful to direct effort improving the mis-
reporting of the number of arguments given versus those required for
instance methods:
  >>> a.f(1, 2)
  TypeError: f() takes exactly 1 argument (3 given)
"""
