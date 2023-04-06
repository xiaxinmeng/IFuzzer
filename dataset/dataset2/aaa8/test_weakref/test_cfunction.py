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
def test_cfunction():
    import _testcapi
    create_cfunction = _testcapi.create_cfunction
    f = create_cfunction()
    wr = weakref.ref(f)
    ReferencesTestCase.assertIs(wr(), f)
    del f
    ReferencesTestCase.assertIsNone(wr())
    ReferencesTestCase.check_basic_ref(create_cfunction)
    ReferencesTestCase.check_basic_callback(create_cfunction)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_cfunction()
