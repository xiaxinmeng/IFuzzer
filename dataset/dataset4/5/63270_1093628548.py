from __future__ import print_function

import weakref

class Class(object):
     def __init__(self, value):
         self.value = value
     def __iadd__(self, value):
         self.value += value
         return self

c = Class(1)

p = weakref.proxy(c)

print('p.value', p.value)
print('type(p)', type(p))