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

def test_cycle_through_dict():

    class X(dict):

        def __init__(ClassPropertiesAndMethods):
            dict.__init__(ClassPropertiesAndMethods)
            ClassPropertiesAndMethods.__dict__ = ClassPropertiesAndMethods
    x = X()
    x.attr = 42
    wr = weakref.ref(x)
    del x
    support.gc_collect()
    ClassPropertiesAndMethods.assertIsNone(wr())
    for o in gc.get_objects():
        ClassPropertiesAndMethods.assertIsNot(type(o), X)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_cycle_through_dict()
