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

def test_vicious_descriptor_nonsense():

    class Evil(object):

        def __hash__(ClassPropertiesAndMethods):
            return hash('attr')

        def __eq__(ClassPropertiesAndMethods, other):
            try:
                del C.attr
            except AttributeError:
                pass
            return 0

    class Descr(object):

        def __get__(ClassPropertiesAndMethods, ob, type=None):
            return 1

    class C(object):
        attr = Descr()
    c = C()
    c.__dict__[Evil()] = 0
    ClassPropertiesAndMethods.assertEqual(c.attr, 1)
    support.gc_collect()
    ClassPropertiesAndMethods.assertNotHasAttr(c, 'attr')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_vicious_descriptor_nonsense()
