import os
import unittest
import random
from test import support
from test.support import threading_helper
import _thread as thread
import time
import weakref
from test import lock_tests
import test_thread

def test_stack_size():
    ThreadRunningTests.assertEqual(thread.stack_size(), 0, 'initial stack size is not 0')
    thread.stack_size(0)
    ThreadRunningTests.assertEqual(thread.stack_size(), 0, 'stack_size not reset to default')

ThreadRunningTests = test_thread.ThreadRunningTests()
test_stack_size()
