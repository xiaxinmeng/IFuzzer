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

def test_subclass_right_op():

    class B(int):

        def __floordiv__(ClassPropertiesAndMethods, other):
            return 'B.__floordiv__'

        def __rfloordiv__(ClassPropertiesAndMethods, other):
            return 'B.__rfloordiv__'
    ClassPropertiesAndMethods.assertEqual(B(1) // 1, 'B.__floordiv__')
    ClassPropertiesAndMethods.assertEqual(1 // B(1), 'B.__rfloordiv__')

    class C(object):

        def __floordiv__(ClassPropertiesAndMethods, other):
            return 'C.__floordiv__'

        def __rfloordiv__(ClassPropertiesAndMethods, other):
            return 'C.__rfloordiv__'
    ClassPropertiesAndMethods.assertEqual(C() // 1, 'C.__floordiv__')
    ClassPropertiesAndMethods.assertEqual(1 // C(), 'C.__rfloordiv__')

    class D(C):

        def __floordiv__(ClassPropertiesAndMethods, other):
            return 'D.__floordiv__'

        def __rfloordiv__(ClassPropertiesAndMethods, other):
            return 'D.__rfloordiv__'
    ClassPropertiesAndMethods.assertEqual(D() // C(), 'D.__floordiv__')
    ClassPropertiesAndMethods.assertEqual(C() // D(), 'D.__rfloordiv__')

    class E(C):
        pass
    ClassPropertiesAndMethods.assertEqual(E.__rfloordiv__, C.__rfloordiv__)
    ClassPropertiesAndMethods.assertEqual(E() // 1, 'C.__floordiv__')
    ClassPropertiesAndMethods.assertEqual(1 // E(), 'C.__rfloordiv__')
    ClassPropertiesAndMethods.assertEqual(E() // C(), 'C.__floordiv__')
    ClassPropertiesAndMethods.assertEqual(C() // E(), 'C.__floordiv__')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_subclass_right_op()
