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

def test_rmul():

    class C(object):

        def __mul__(ClassPropertiesAndMethods, other):
            return 'mul'

        def __rmul__(ClassPropertiesAndMethods, other):
            return 'rmul'
    a = C()
    ClassPropertiesAndMethods.assertEqual(a * 2, 'mul')
    ClassPropertiesAndMethods.assertEqual(a * 2.2, 'mul')
    ClassPropertiesAndMethods.assertEqual(2 * a, 'rmul')
    ClassPropertiesAndMethods.assertEqual(2.2 * a, 'rmul')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_rmul()
