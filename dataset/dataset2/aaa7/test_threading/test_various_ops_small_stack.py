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

def test_various_ops_small_stack():
    if verbose:
        print('with 256 KiB thread stack size...')
    try:
        threading.stack_size(262144)
    except _thread.error:
        raise unittest.SkipTest('platform does not support changing thread stack size')
    ThreadTests.test_various_ops()
    threading.stack_size(0)

ThreadTests = test_threading.ThreadTests()
test_various_ops_small_stack()
