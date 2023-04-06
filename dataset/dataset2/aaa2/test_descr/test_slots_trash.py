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

def test_slots_trash():

    class trash(object):
        __slots__ = ['x']

        def __init__(ClassPropertiesAndMethods, x):
            ClassPropertiesAndMethods.x = x
    o = None
    for i in range(50000):
        o = trash(o)
    del o

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_slots_trash()
