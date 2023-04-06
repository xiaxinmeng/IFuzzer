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

def test_lists():
    OperatorsTest.binop_test([1], [2], [1, 2], 'a+b', '__add__')
    OperatorsTest.binop_test([1, 2, 3], 2, 1, 'b in a', '__contains__')
    OperatorsTest.binop_test([1, 2, 3], 4, 0, 'b in a', '__contains__')
    OperatorsTest.binop_test([1, 2, 3], 1, 2, 'a[b]', '__getitem__')
    OperatorsTest.sliceop_test([1, 2, 3], 0, 2, [1, 2], 'a[b:c]', '__getitem__')
    OperatorsTest.setop_test([1], [2], [1, 2], 'a+=b', '__iadd__')
    OperatorsTest.setop_test([1, 2], 3, [1, 2, 1, 2, 1, 2], 'a*=b', '__imul__')
    OperatorsTest.unop_test([1, 2, 3], 3, 'len(a)', '__len__')
    OperatorsTest.binop_test([1, 2], 3, [1, 2, 1, 2, 1, 2], 'a*b', '__mul__')
    OperatorsTest.binop_test([1, 2], 3, [1, 2, 1, 2, 1, 2], 'b*a', '__rmul__')
    OperatorsTest.set2op_test([1, 2], 1, 3, [1, 3], 'a[b]=c', '__setitem__')
    OperatorsTest.setsliceop_test([1, 2, 3, 4], 1, 3, [5, 6], [1, 5, 6, 4], 'a[b:c]=d', '__setitem__')

OperatorsTest = test_descr.OperatorsTest()
test_lists()
