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

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_properties_doc_attrib():

    class E(object):

        def getter(ClassPropertiesAndMethods):
            """getter method"""
            return 0

        def setter(ClassPropertiesAndMethods_, value):
            """setter method"""
            pass
        prop = property(getter)
        ClassPropertiesAndMethods.assertEqual(prop.__doc__, 'getter method')
        prop2 = property(fset=setter)
        ClassPropertiesAndMethods.assertEqual(prop2.__doc__, None)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_properties_doc_attrib()
