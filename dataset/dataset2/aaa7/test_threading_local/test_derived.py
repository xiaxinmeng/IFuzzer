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

def test_derived():
    import time

    class Local(BaseLocalTest._local):

        def __init__(BaseLocalTest):
            time.sleep(0.01)
    local = Local()

    def f(i):
        local.x = i
        BaseLocalTest.assertEqual(local.x, i)
    with threading_helper.start_threads((threading.Thread(target=f, args=(i,)) for i in range(10))):
        pass

BaseLocalTest = test_threading_local.BaseLocalTest()
test_derived()
