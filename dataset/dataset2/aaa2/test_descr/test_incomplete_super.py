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

def test_incomplete_super():
    """
        Attrubute lookup on a super object must be aware that
        its target type can be uninitialized (type->tp_mro == NULL).
        """

    class M(test_descr.DebugHelperMeta):

        def mro(cls):
            if cls.__mro__ is None:
                with MroTest.assertRaises(AttributeError):
                    super(cls, cls).xxx
            return type.mro(cls)

    class A(metaclass=M):
        pass

MroTest = test_descr.MroTest()
test_incomplete_super()
