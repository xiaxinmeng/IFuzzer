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

def test_str_subclass_as_dict_key():

    class cistr(str):
        """Subclass of str that computes __eq__ case-insensitively.

            Also computes a hash code of the string in canonical form.
            """

        def __init__(ClassPropertiesAndMethods, value):
            ClassPropertiesAndMethods.canonical = value.lower()
            ClassPropertiesAndMethods.hashcode = hash(ClassPropertiesAndMethods.canonical)

        def __eq__(ClassPropertiesAndMethods, other):
            if not isinstance(other, cistr):
                other = cistr(other)
            return ClassPropertiesAndMethods.canonical == other.canonical

        def __hash__(ClassPropertiesAndMethods):
            return ClassPropertiesAndMethods.hashcode
    ClassPropertiesAndMethods.assertEqual(cistr('ABC'), 'abc')
    ClassPropertiesAndMethods.assertEqual('aBc', cistr('ABC'))
    ClassPropertiesAndMethods.assertEqual(str(cistr('ABC')), 'ABC')
    d = {cistr('one'): 1, cistr('two'): 2, cistr('tHree'): 3}
    ClassPropertiesAndMethods.assertEqual(d[cistr('one')], 1)
    ClassPropertiesAndMethods.assertEqual(d[cistr('tWo')], 2)
    ClassPropertiesAndMethods.assertEqual(d[cistr('THrEE')], 3)
    ClassPropertiesAndMethods.assertIn(cistr('ONe'), d)
    ClassPropertiesAndMethods.assertEqual(d.get(cistr('thrEE')), 3)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_str_subclass_as_dict_key()
