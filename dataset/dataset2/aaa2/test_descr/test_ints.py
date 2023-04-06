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

def test_ints():
    OperatorsTest.number_operators(100, 3)
    OperatorsTest.assertEqual(1 .__bool__(), 1)
    OperatorsTest.assertEqual(0 .__bool__(), 0)

    class C(int):

        def __add__(OperatorsTest, other):
            return NotImplemented
    OperatorsTest.assertEqual(C(5), 5)
    try:
        C() + ''
    except TypeError:
        pass
    else:
        OperatorsTest.fail('NotImplemented should have caused TypeError')

OperatorsTest = test_descr.OperatorsTest()
test_ints()
