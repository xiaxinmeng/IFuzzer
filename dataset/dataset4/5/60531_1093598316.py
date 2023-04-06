pycon
"""
Python 2.7.3 (default, Apr 12 2012, 13:11:53) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> try :
...   1/0
... except :
...   try :
...     raise RuntimeError("TEST")
...   except :
...     pass
...   raise
... 
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
RuntimeError: TEST
"""

"""
Python 3.3.0 (default, Oct  2 2012, 02:07:16) 
[GCC 4.4.3] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> try :
...   1/0
... except :
...   try :
...     raise RuntimeError("TEST")
...   except :
...     pass
...   raise
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
"""
