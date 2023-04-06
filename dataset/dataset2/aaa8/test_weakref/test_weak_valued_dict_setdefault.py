import gc
import sys
import unittest
import collections
import weakref
import operator
import contextlib
import copy
import threading
import time
import random
from test import support
from test.support import script_helper, ALWAYS_EQ
import _testcapi
import gc
import gc
import gc
import gc
import gc
import gc
import gc
from test import mapping_tests
import test_weakref

def test_weak_valued_dict_setdefault():
    MappingTestCase.check_setdefault(weakref.WeakValueDictionary, 'key', test_weakref.C(), test_weakref.C())

MappingTestCase = test_weakref.MappingTestCase()
test_weak_valued_dict_setdefault()
