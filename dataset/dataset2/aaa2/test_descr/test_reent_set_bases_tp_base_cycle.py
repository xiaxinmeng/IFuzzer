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

def test_reent_set_bases_tp_base_cycle():
    """
        type_set_bases must check for an inheritance cycle not only through
        MRO of the type, which may be not yet updated in case of reentrance,
        but also through tp_base chain, which is assigned before diving into
        inner calls to mro().

        Otherwise, the following snippet can loop forever:
            do {
                // ...
                type = type->tp_base;
            } while (type != NULL);

        Functions that rely on tp_base (like solid_base and PyType_IsSubtype)
        would not be happy in that case, causing a stack overflow.
        """

    class M(test_descr.DebugHelperMeta):

        def mro(cls):
            if MroTest.ready:
                if cls.__name__ == 'B1':
                    B2.__bases__ = (B1,)
                if cls.__name__ == 'B2':
                    B1.__bases__ = (B2,)
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B1(A):
        pass

    class B2(A):
        pass
    MroTest.ready = True
    with MroTest.assertRaises(TypeError):
        B1.__bases__ += ()

MroTest = test_descr.MroTest()
MroTest.setUp()
test_reent_set_bases_tp_base_cycle()
