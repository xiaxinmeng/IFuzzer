pycon
"""
Python 3.2 (r32:88445, Feb 21 2011, 13:34:07)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> >>> f=open("file.pickle", mode="rb").read()
>>> >>> len(f)
9847316
>>> >>> b=pickle.loads(f,encoding="latin1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operation forbidden on released memoryview object
"""
