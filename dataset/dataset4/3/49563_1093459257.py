pycon
"""
>>> import StringIO
>>> s=StringIO.StringIO("xxx")
>>> s.fileno()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: StringIO instance has no attribute 'fileno'
"""
