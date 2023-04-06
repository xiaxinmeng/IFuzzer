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

def test_newslots():

    class C(list):

        def __new__(cls):
            ClassPropertiesAndMethods = list.__new__(cls)
            ClassPropertiesAndMethods.foo = 1
            return ClassPropertiesAndMethods

        def __init__(ClassPropertiesAndMethods):
            ClassPropertiesAndMethods.foo = ClassPropertiesAndMethods.foo + 2
    a = C()
    ClassPropertiesAndMethods.assertEqual(a.foo, 3)
    ClassPropertiesAndMethods.assertEqual(a.__class__, C)

    class D(C):
        pass
    b = D()
    ClassPropertiesAndMethods.assertEqual(b.foo, 3)
    ClassPropertiesAndMethods.assertEqual(b.__class__, D)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_newslots()
