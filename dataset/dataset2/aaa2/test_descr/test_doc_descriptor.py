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

def test_doc_descriptor():

    class DocDescr(object):

        def __get__(ClassPropertiesAndMethods, object, otype):
            if object:
                object = object.__class__.__name__ + ' instance'
            if otype:
                otype = otype.__name__
            return 'object=%s; type=%s' % (object, otype)

    class OldClass:
        __doc__ = DocDescr()

    class NewClass(object):
        __doc__ = DocDescr()
    ClassPropertiesAndMethods.assertEqual(OldClass.__doc__, 'object=None; type=OldClass')
    ClassPropertiesAndMethods.assertEqual(OldClass().__doc__, 'object=OldClass instance; type=OldClass')
    ClassPropertiesAndMethods.assertEqual(NewClass.__doc__, 'object=None; type=NewClass')
    ClassPropertiesAndMethods.assertEqual(NewClass().__doc__, 'object=NewClass instance; type=NewClass')

ClassPropertiesAndMethods = test_descr.ClassPropertiesAndMethods()
test_doc_descriptor()
