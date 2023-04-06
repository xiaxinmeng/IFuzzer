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

def test_incomplete_extend():
    """
        Extending an unitialized type with type->tp_mro == NULL must
        throw a reasonable TypeError exception, instead of failing
        with PyErr_BadInternalCall.
        """

    class M(test_descr.DebugHelperMeta):

        def mro(cls):
            if cls.__mro__ is None and cls.__name__ != 'X':
                with MroTest.assertRaises(TypeError):

                    class X(cls):
                        pass
            return type.mro(cls)

    class A(metaclass=M):
        pass

MroTest = test_descr.MroTest()
test_incomplete_extend()
