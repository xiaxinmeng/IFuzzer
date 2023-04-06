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

def test_gc_main_module_at_shutdown():
    code = "if 1:\n            class C:\n                def __del__(GCTests):\n                    print('__del__ called')\n            l = [C()]\n            l.append(l)\n            "
    (rc, out, err) = assert_python_ok('-c', code)
    GCTests.assertEqual(out.strip(), b'__del__ called')

GCTests = test_gc.GCTests()
test_gc_main_module_at_shutdown()
