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

def test_make_weak_keyed_dict_repr():
    dict = weakref.WeakKeyDictionary()
    MappingTestCase.assertRegex(repr(dict), '<WeakKeyDictionary at 0x.*>')

MappingTestCase = test_weakref.MappingTestCase()
test_make_weak_keyed_dict_repr()
