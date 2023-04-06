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

def test_qualname_dict():
    ns = {'__qualname__': 'some.name'}
    tp = type('Foo', (), ns)
    ClassPropertiesAndMethods.assertEqual(tp.__qualname__, 'some.name')
    ClassPropertiesAndMethods.assertNotIn('__qualname__', tp.__dict__)
    ClassPropertiesAndMethods.assertEqual(ns, {'__qualname__': 'some.name'})
    ns = {'__qualname__': 1}
    ClassPropertiesAndMethods.assertRaises(TypeError, type, 'Foo', (), ns)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_qualname_dict()
