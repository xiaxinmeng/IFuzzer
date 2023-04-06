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

def test_carloverre_multi_inherit_invalid():

    class A(type):

        def __setattr__(cls, key, value):
            object.__setattr__(cls, key, value)

    class B:
        pass

    class C(B, A):
        pass
    obj = C('D', (object,), {})
    try:
        obj.test = True
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail('setattr through indirect base types should be rejected')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_carloverre_multi_inherit_invalid()
