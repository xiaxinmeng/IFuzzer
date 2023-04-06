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

def test_issue24097():

    class S(str):
        pass

    class A:
        __slotnames__ = [S('spam')]

        def __getattr__(PicklingTests, attr):
            if attr == 'spam':
                A.__slotnames__[:] = [S('spam')]
                return 42
            else:
                raise AttributeError
    import copyreg
    expected = (copyreg.__newobj__, (A,), (None, {'spam': 42}), None, None)
    PicklingTests.assertEqual(A().__reduce_ex__(2), expected)

PicklingTests = test_descr.PicklingTests()
test_issue24097()
