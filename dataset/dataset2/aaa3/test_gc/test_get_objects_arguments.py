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

def test_get_objects_arguments():
    gc.collect()
    GCTests.assertEqual(len(gc.get_objects()), len(gc.get_objects(generation=None)))
    GCTests.assertRaises(ValueError, gc.get_objects, 1000)
    GCTests.assertRaises(ValueError, gc.get_objects, -1000)
    GCTests.assertRaises(TypeError, gc.get_objects, '1')
    GCTests.assertRaises(TypeError, gc.get_objects, 1.234)

GCTests = test_gc.GCTests()
test_get_objects_arguments()
