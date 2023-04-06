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

def test_init():

    class Foo(object):

        def __init__(ClassPropertiesAndMethods):
            return 10
    try:
        Foo()
    except TypeError:
        pass
    else:
        ClassPropertiesAndMethods.fail('did not test __init__() for None return')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_init()
