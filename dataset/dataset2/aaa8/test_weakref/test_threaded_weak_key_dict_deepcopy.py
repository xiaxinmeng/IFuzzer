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

def test_threaded_weak_key_dict_deepcopy():
    MappingTestCase.check_threaded_weak_dict_copy(weakref.WeakKeyDictionary, True)

MappingTestCase = test_weakref.MappingTestCase()
test_threaded_weak_key_dict_deepcopy()
