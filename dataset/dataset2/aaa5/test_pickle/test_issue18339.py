from _compat_pickle import IMPORT_MAPPING, REVERSE_IMPORT_MAPPING, NAME_MAPPING, REVERSE_NAME_MAPPING
import builtins
import pickle
import io
import collections
import struct
import sys
import weakref
import unittest
from test import support
from test.support import import_helper
from test.pickletester import AbstractHookTests
from test.pickletester import AbstractUnpickleTests
from test.pickletester import AbstractPickleTests
from test.pickletester import AbstractPickleModuleTests
from test.pickletester import AbstractPersistentPicklerTests
from test.pickletester import AbstractIdentityPersistentPicklerTests
from test.pickletester import AbstractPicklerUnpicklerObjectTests
from test.pickletester import AbstractDispatchTableTests
from test.pickletester import AbstractCustomPicklerClass
from test.pickletester import BigmemPickleTests
import _pickle
from _pickle import dump, dumps, load, loads, Pickler, Unpickler
import test_pickle

def test_issue18339():
    unpickler = CPicklerUnpicklerObjectTests.unpickler_class(io.BytesIO())
    with CPicklerUnpicklerObjectTests.assertRaises(TypeError):
        unpickler.memo = object
    with CPicklerUnpicklerObjectTests.assertRaises(ValueError):
        unpickler.memo = {-1: None}
    unpickler.memo = {1: None}

CPicklerUnpicklerObjectTests = test_pickle.CPicklerUnpicklerObjectTests()
test_issue18339()
