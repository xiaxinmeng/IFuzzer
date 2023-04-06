pycon
"""
>>> class Foo(object):
...    def _get(self):
...        return 'the docstring'
...    __doc__ = property(_get)
...
>>> print Foo().__doc__
the docstring
>>> print Foo.__doc__
<property object at 0xb7b3a234>
>>>
"""
