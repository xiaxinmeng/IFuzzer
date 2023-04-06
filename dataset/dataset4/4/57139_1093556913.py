def f0():
  s = """select
some sql
from
somewhere;
-- cannot be reindented"""

def f1():
  """ Multiline 
  text docstring
  should be reindented """

def f2():
  """ should example be reindented inside docstring?
  if f2():
    print "great"
  """

def f3():
  """ # should doctest be reindented inside docstring?
  >>> if f3():
  ...   print "yes"
  ... else:
  ...   print "no"
  ...
  no
  """