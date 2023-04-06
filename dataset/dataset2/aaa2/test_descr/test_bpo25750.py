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

@unittest.skipIf(_testcapi is None, 'need the _testcapi module')
def test_bpo25750():

    class Descr:
        __get__ = _testcapi.bad_get

    class X:
        descr = Descr()

        def __new__(cls):
            cls.descr = None
            cls.lst = [2 ** i for i in range(10000)]
    X.descr

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_bpo25750()
