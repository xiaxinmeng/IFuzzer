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

def test_python_lists():

    class C(list):

        def __getitem__(ClassPropertiesAndMethods, i):
            if isinstance(i, slice):
                return (i.start, i.stop)
            return list.__getitem__(ClassPropertiesAndMethods, i) + 100
    a = C()
    a.extend([0, 1, 2])
    ClassPropertiesAndMethods.assertEqual(a[0], 100)
    ClassPropertiesAndMethods.assertEqual(a[1], 101)
    ClassPropertiesAndMethods.assertEqual(a[2], 102)
    ClassPropertiesAndMethods.assertEqual(a[100:200], (100, 200))

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_python_lists()
