import sys
import unittest
from doctest import DocTestSuite
from test import support
from test.support import threading_helper
import weakref
import gc
import _thread
import threading
import _threading_local
import time
import test_threading_local

def test_cycle_collection():

    class X:
        pass
    x = X()
    x.local = BaseLocalTest._local()
    x.local.x = x
    wr = weakref.ref(x)
    del x
    gc.collect()
    BaseLocalTest.assertIsNone(wr())

BaseLocalTest = test_threading_local.BaseLocalTest()
test_cycle_collection()
