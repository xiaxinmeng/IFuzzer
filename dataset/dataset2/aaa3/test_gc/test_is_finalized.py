import unittest
import unittest.mock
from test.support import verbose, refcount_test, run_unittest, cpython_only
from test.support.import_helper import import_module
from test.support.os_helper import temp_dir, TESTFN, unlink
from test.support.script_helper import assert_python_ok, make_script
from test.support import threading_helper
import gc
import sys
import sysconfig
import textwrap
import threading
import time
import weakref
from _testcapi import with_tp_del
from _testcapi import ContainerNoGC
import subprocess
import subprocess
import test_gc

def test_is_finalized():
    GCTests.assertFalse(gc.is_finalized(3))
    storage = []

    class Lazarus:

        def __del__(GCTests):
            storage.append(GCTests)
    lazarus = Lazarus()
    GCTests.assertFalse(gc.is_finalized(lazarus))
    del lazarus
    gc.collect()
    lazarus = storage.pop()
    GCTests.assertTrue(gc.is_finalized(lazarus))

GCTests = test_gc.GCTests()
test_is_finalized()
