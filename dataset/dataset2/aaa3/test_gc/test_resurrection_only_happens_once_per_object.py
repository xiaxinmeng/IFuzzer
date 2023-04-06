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

def test_resurrection_only_happens_once_per_object():

    class A:

        def __init__(GCTests):
            GCTests.me = GCTests

    class Lazarus(A):
        resurrected = 0
        resurrected_instances = []

        def __del__(GCTests):
            Lazarus.resurrected += 1
            Lazarus.resurrected_instances.append(GCTests)
    gc.collect()
    gc.disable()
    laz = Lazarus()
    GCTests.assertEqual(Lazarus.resurrected, 0)
    del laz
    gc.collect()
    GCTests.assertEqual(Lazarus.resurrected, 1)
    GCTests.assertEqual(len(Lazarus.resurrected_instances), 1)
    Lazarus.resurrected_instances.clear()
    GCTests.assertEqual(Lazarus.resurrected, 1)
    gc.collect()
    GCTests.assertEqual(Lazarus.resurrected, 1)
    gc.enable()

GCTests = test_gc.GCTests()
test_resurrection_only_happens_once_per_object()
