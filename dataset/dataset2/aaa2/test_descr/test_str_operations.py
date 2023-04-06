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

def test_str_operations():
    try:
        'a' + 5
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'' + 5 doesn't raise TypeError")
    try:
        ''.split('')
    except ValueError:
        pass
    else:
        ClassPropertiesAndMethods.fail("''.split('') doesn't raise ValueError")
    try:
        ''.join([0])
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail("''.join([0]) doesn't raise TypeError")
    try:
        ''.rindex('5')
    except ValueError:
        pass
    else:
        ClassPropertiesAndMethods.fail("''.rindex('5') doesn't raise ValueError")
    try:
        '%(n)s' % None
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'%(n)s' % None doesn't raise TypeError")
    try:
        '%(n' % {}
    except ValueError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'%(n' % {} '' doesn't raise ValueError")
    try:
        '%*s' % 'abc'
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'%*s' % ('abc') doesn't raise TypeError")
    try:
        '%*.*s' % ('abc', 5)
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'%*.*s' % ('abc', 5) doesn't raise TypeError")
    try:
        '%s' % (1, 2)
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'%s' % (1, 2) doesn't raise TypeError")
    try:
        '%' % None
    except ValueError:
        pass
    else:
        ClassPropertiesAndMethods.fail("'%' % None doesn't raise ValueError")
    ClassPropertiesAndMethods.assertEqual('534253'.isdigit(), 1)
    ClassPropertiesAndMethods.assertEqual('534253x'.isdigit(), 0)
    ClassPropertiesAndMethods.assertEqual('%c' % 5, '\x05')
    ClassPropertiesAndMethods.assertEqual('%c' % '5', '5')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_str_operations()
