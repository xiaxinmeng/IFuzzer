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

def test_binary_operator_override():

    class I(int):

        def __repr__(ClassPropertiesAndMethods):
            return 'I(%r)' % int(ClassPropertiesAndMethods)

        def __add__(ClassPropertiesAndMethods, other):
            return I(int(ClassPropertiesAndMethods) + int(other))
        __radd__ = __add__

        def __pow__(ClassPropertiesAndMethods, other, mod=None):
            if mod is None:
                return I(pow(int(ClassPropertiesAndMethods), int(other)))
            else:
                return I(pow(int(ClassPropertiesAndMethods), int(other), int(mod)))

        def __rpow__(ClassPropertiesAndMethods, other, mod=None):
            if mod is None:
                return I(pow(int(other), int(ClassPropertiesAndMethods), mod))
            else:
                return I(pow(int(other), int(ClassPropertiesAndMethods), int(mod)))
    ClassPropertiesAndMethods.assertEqual(repr(I(1) + I(2)), 'I(3)')
    ClassPropertiesAndMethods.assertEqual(repr(I(1) + 2), 'I(3)')
    ClassPropertiesAndMethods.assertEqual(repr(1 + I(2)), 'I(3)')
    ClassPropertiesAndMethods.assertEqual(repr(I(2) ** I(3)), 'I(8)')
    ClassPropertiesAndMethods.assertEqual(repr(2 ** I(3)), 'I(8)')
    ClassPropertiesAndMethods.assertEqual(repr(I(2) ** 3), 'I(8)')
    ClassPropertiesAndMethods.assertEqual(repr(pow(I(2), I(3), I(5))), 'I(3)')

    class S(str):

        def __eq__(ClassPropertiesAndMethods, other):
            return ClassPropertiesAndMethods.lower() == other.lower()

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_binary_operator_override()
