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

def test_copy_setstate():
    import copy

    class C(object):

        def __init__(ClassPropertiesAndMethods, foo=None):
            ClassPropertiesAndMethods.foo = foo
            ClassPropertiesAndMethods.__foo = foo

        def setfoo(ClassPropertiesAndMethods, foo=None):
            ClassPropertiesAndMethods.foo = foo

        def getfoo(ClassPropertiesAndMethods):
            return ClassPropertiesAndMethods.__foo

        def __getstate__(ClassPropertiesAndMethods):
            return [ClassPropertiesAndMethods.foo]

        def __setstate__(ClassPropertiesAndMethods_, lst):
            ClassPropertiesAndMethods.assertEqual(len(lst), 1)
            ClassPropertiesAndMethods_.__foo = ClassPropertiesAndMethods_.foo = lst[0]
    a = C(42)
    a.setfoo(24)
    ClassPropertiesAndMethods.assertEqual(a.foo, 24)
    ClassPropertiesAndMethods.assertEqual(a.getfoo(), 42)
    b = copy.copy(a)
    ClassPropertiesAndMethods.assertEqual(b.foo, 24)
    ClassPropertiesAndMethods.assertEqual(b.getfoo(), 24)
    b = copy.deepcopy(a)
    ClassPropertiesAndMethods.assertEqual(b.foo, 24)
    ClassPropertiesAndMethods.assertEqual(b.getfoo(), 24)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_copy_setstate()
