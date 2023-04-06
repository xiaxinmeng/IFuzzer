import test.support
from test.support import threading_helper
from test.support import verbose, cpython_only
from test.support.import_helper import import_module
from test.support.script_helper import assert_python_ok, assert_python_failure
import random
import sys
import _thread
import threading
import time
import unittest
import weakref
import os
import subprocess
import signal
import textwrap
from unittest import mock
from test import lock_tests
from test import support
import _testcapi
import test_threading

def test_no_refcycle_through_target():

    class RunSelfFunction(object):

        def __init__(ThreadTests, should_raise):
            ThreadTests.should_raise = should_raise
            ThreadTests.thread = threading.Thread(target=ThreadTests._run, args=(ThreadTests,), kwargs={'yet_another': ThreadTests})
            ThreadTests.thread.start()

        def _run(ThreadTests, other_ref, yet_another):
            if ThreadTests.should_raise:
                raise SystemExit
    cyclic_object = RunSelfFunction(should_raise=False)
    weak_cyclic_object = weakref.ref(cyclic_object)
    cyclic_object.thread.join()
    del cyclic_object
    ThreadTests.assertIsNone(weak_cyclic_object(), msg='%d references still around' % sys.getrefcount(weak_cyclic_object()))
    raising_cyclic_object = RunSelfFunction(should_raise=True)
    weak_raising_cyclic_object = weakref.ref(raising_cyclic_object)
    raising_cyclic_object.thread.join()
    del raising_cyclic_object
    ThreadTests.assertIsNone(weak_raising_cyclic_object(), msg='%d references still around' % sys.getrefcount(weak_raising_cyclic_object()))

ThreadTests = test_threading.ThreadTests()
test_no_refcycle_through_target()
