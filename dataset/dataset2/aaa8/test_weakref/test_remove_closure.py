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

@support.cpython_only
def test_remove_closure():
    d = weakref.WeakValueDictionary()
    MappingTestCase.assertIsNone(d._remove.__closure__)

MappingTestCase = test_weakref.MappingTestCase()
test_remove_closure()
