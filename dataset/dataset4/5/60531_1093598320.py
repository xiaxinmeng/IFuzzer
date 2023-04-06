pycon
"""
Python 2.7.3 (default, Apr 12 2012, 13:11:53) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> try :
...   1/0
... except BaseException as e :
...   try :
...     raise
...   finally :
...     try :
...       raise RuntimeError("TEST")
...     except :
...       pass
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: integer division or modulo by zero
"""
