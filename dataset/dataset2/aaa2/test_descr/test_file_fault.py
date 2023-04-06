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

def test_file_fault():
    test_stdout = sys.stdout

    class StdoutGuard:

        def __getattr__(ClassPropertiesAndMethods, attr):
            sys.stdout = sys.__stdout__
            raise RuntimeError('Premature access to sys.stdout.%s' % attr)
    sys.stdout = StdoutGuard()
    try:
        print('Oops!')
    except RuntimeError:
        pass
    finally:
        sys.stdout = test_stdout

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_file_fault()
