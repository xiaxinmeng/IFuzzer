#!/usr/bin/env python
import sys
sys.path.insert(0, 'Lib')
import timeit
import weakref

class Foo(object): pass
def setup():
    L = [Foo() for i in range(1000)]
    global d
    d = weakref.WeakValueDictionary(enumerate(L))
    del L[:500] # have some dead weakrefs

def do():
    d.values()