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

def test_special_method_lookup():
    protocols = range(pickle.HIGHEST_PROTOCOL + 1)

    class Picky:

        def __getstate__(ClassPropertiesAndMethods):
            return {}

        def __getattr__(ClassPropertiesAndMethods, attr):
            if attr in ('__getnewargs__', '__getnewargs_ex__'):
                raise AssertionError(attr)
            return None
    for protocol in protocols:
        state = {} if protocol >= 2 else None
        ClassPropertiesAndMethods._check_reduce(protocol, Picky(), state=state)

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
ClassPropertiesAndMethods.setUp()
test_special_method_lookup()
