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

@unittest.skipIf(hasattr(sys, 'gettrace') and sys.gettrace(), 'trace function introduces __local__')
def test_iter_values():
    it = DictProxyTests.C.__dict__.values()
    DictProxyTests.assertNotIsInstance(it, list)
    values = list(it)
    DictProxyTests.assertEqual(len(values), 5)

DictProxyTests = test_descr.DictProxyTests()
DictProxyTests.setUp()
test_iter_values()
