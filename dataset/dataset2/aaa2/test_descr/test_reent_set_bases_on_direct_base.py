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

def test_reent_set_bases_on_direct_base():
    """
        Similar to test_reent_set_bases_on_base, but may crash differently.
        """

    class M(test_descr.DebugHelperMeta):

        def mro(cls):
            base = cls.__bases__[0]
            if base is not object:
                if MroTest.step_until(5):
                    base.__bases__ += ()
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B(A):
        pass

    class C(B):
        pass

MroTest = test_descr.MroTest()
MroTest.setUp()
test_reent_set_bases_on_direct_base()
