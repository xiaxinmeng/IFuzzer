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

def test_reent_set_bases_on_base():
    """
        Deep reentrancy must not over-decref old_mro.
        """

    class M(test_descr.DebugHelperMeta):

        def mro(cls):
            if cls.__mro__ is not None and cls.__name__ == 'B':
                if MroTest.step_until(10):
                    A.__bases__ += ()
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B(A):
        pass
    B.__bases__ += ()

MroTest = test_descr.MroTest()
MroTest.setUp()
test_reent_set_bases_on_base()
