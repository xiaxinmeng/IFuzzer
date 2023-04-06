import builtins
import copyreg
import gc
import itertools
import math
import pickle
import random
import string
import sys
import types
import unittest
import warnings
import weakref
from copy import deepcopy
from test import support
import _testcapi
import copy, xxsubtype as spam
import xxsubtype as spam
import copy, xxsubtype as spam
import xxsubtype as spam
import abc
import xxsubtype as spam
import xxsubtype as spam
import weakref
import _testcapi
from _io import FileIO
import binascii
import binascii
import io
from types import ModuleType as M
import copy
import weakref
import operator
import copyreg
import test_descr

def test_overloading():

    class B(object):
        """Intermediate class because object doesn't have a __setattr__"""

    class C(B):

        def __getattr__(ClassPropertiesAndMethods, name):
            if name == 'foo':
                return ('getattr', name)
            else:
                raise AttributeError

        def __setattr__(ClassPropertiesAndMethods, name, value):
            if name == 'foo':
                ClassPropertiesAndMethods.setattr = (name, value)
            else:
                return B.__setattr__(ClassPropertiesAndMethods, name, value)

        def __delattr__(ClassPropertiesAndMethods, name):
            if name == 'foo':
                ClassPropertiesAndMethods.delattr = name
            else:
                return B.__delattr__(ClassPropertiesAndMethods, name)

        def __getitem__(ClassPropertiesAndMethods, key):
            return ('getitem', key)

        def __setitem__(ClassPropertiesAndMethods, key, value):
            ClassPropertiesAndMethods.setitem = (key, value)

        def __delitem__(ClassPropertiesAndMethods, key):
            ClassPropertiesAndMethods.delitem = key
    a = C()
    ClassPropertiesAndMethods.assertEqual(a.foo, ('getattr', 'foo'))
    a.foo = 12
    ClassPropertiesAndMethods.assertEqual(a.setattr, ('foo', 12))
    del a.foo
    ClassPropertiesAndMethods.assertEqual(a.delattr, 'foo')
    ClassPropertiesAndMethods.assertEqual(a[12], ('getitem', 12))
    a[12] = 21
    ClassPropertiesAndMethods.assertEqual(a.setitem, (12, 21))
    del a[12]
    ClassPropertiesAndMethods.assertEqual(a.delitem, 12)
    ClassPropertiesAndMethods.assertEqual(a[0:10], ('getitem', slice(0, 10)))
    a[0:10] = 'foo'
    ClassPropertiesAndMethods.assertEqual(a.setitem, (slice(0, 10), 'foo'))
    del a[0:10]
    ClassPropertiesAndMethods.assertEqual(a.delitem, slice(0, 10))

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_overloading()
