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

def test_mutable_names():

    class C(object):
        pass
    mod = C.__module__
    C.__name__ = 'D'
    ClassPropertiesAndMethods.assertEqual((C.__module__, C.__name__), (mod, 'D'))
    C.__name__ = 'D.E'
    ClassPropertiesAndMethods.assertEqual((C.__module__, C.__name__), (mod, 'D.E'))

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_mutable_names()
