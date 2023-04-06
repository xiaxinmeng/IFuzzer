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

def test_special_unbound_method_types():
    ClassPropertiesAndMethods.assertTrue(list.__add__ == list.__add__)
    ClassPropertiesAndMethods.assertFalse(list.__add__ != list.__add__)
    ClassPropertiesAndMethods.assertFalse(list.__add__ == list.__mul__)
    ClassPropertiesAndMethods.assertTrue(list.__add__ != list.__mul__)
    ClassPropertiesAndMethods.assertNotOrderable(list.__add__, list.__add__)
    ClassPropertiesAndMethods.assertEqual(list.__add__.__name__, '__add__')
    ClassPropertiesAndMethods.assertIs(list.__add__.__objclass__, list)
    ClassPropertiesAndMethods.assertTrue(list.append == list.append)
    ClassPropertiesAndMethods.assertFalse(list.append != list.append)
    ClassPropertiesAndMethods.assertFalse(list.append == list.pop)
    ClassPropertiesAndMethods.assertTrue(list.append != list.pop)
    ClassPropertiesAndMethods.assertNotOrderable(list.append, list.append)
    ClassPropertiesAndMethods.assertEqual(list.append.__name__, 'append')
    ClassPropertiesAndMethods.assertIs(list.append.__objclass__, list)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_special_unbound_method_types()
