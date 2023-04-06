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

@support.refcount_test
def test_refleaks_in_staticmethod___init__():
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    sm = staticmethod(None)
    refs_before = gettotalrefcount()
    for i in range(100):
        sm.__init__(None)
    ClassPropertiesAndMethods.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_refleaks_in_staticmethod___init__()
