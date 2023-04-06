pycon
"""
Python 3.3.0 (default, Oct  2 2012, 02:07:16) 
[GCC 4.4.3] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import inspect
>>> def f(a=None) :
...   pass
... 
>>> inspect.getcallargs(f)
{'a': None}
>>> inspect.getargspec(f)
ArgSpec(args=['a'], varargs=None, keywords=None, defaults=(None,))
>>> inspect.getcallargs(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/inspect.py", line 993, in getcallargs
    spec = getfullargspec(func)
  File "/usr/local/lib/python3.3/inspect.py", line 850, in getfullargspec
    raise TypeError('{!r} is not a Python function'.format(func))
TypeError: <class 'list'> is not a Python function
>>> inspect.getargspec(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/inspect.py", line 823, in getargspec
    getfullargspec(func)
  File "/usr/local/lib/python3.3/inspect.py", line 850, in getfullargspec
    raise TypeError('{!r} is not a Python function'.format(func))
TypeError: <class 'list'> is not a Python function
>>> 
"""
