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

def test_del_newclass():
    thresholds = gc.get_threshold()
    gc.enable()
    gc.set_threshold(1)

    class A(object):

        def __del__(GCTests):
            dir(GCTests)
    a = A()
    del a
    gc.disable()
    gc.set_threshold(*thresholds)

GCTests = test_gc.GCTests()
test_del_newclass()
