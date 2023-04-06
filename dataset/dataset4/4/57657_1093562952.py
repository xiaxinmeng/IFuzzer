pycon
"""
>>> def a() :
...   class b() :
...     pass
...   return b()
... 
>>> c=a()
>>> c
<__main__.a.<locals>.b object at 0xfe37f3ac>
>>> c.__qualname__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'b' object has no attribute '__qualname__'
>>> a
<function a at 0xfe3800bc>
>>> a.__qualname__
'a'
"""
