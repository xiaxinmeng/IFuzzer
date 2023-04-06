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

def test_unraisable_exception():

    def task():
        started.release()
        raise ValueError('task failed')
    started = thread.allocate_lock()
    with support.catch_unraisable_exception() as cm:
        with threading_helper.wait_threads_exit():
            started.acquire()
            thread.start_new_thread(task, ())
            started.acquire()
        ThreadRunningTests.assertEqual(str(cm.unraisable.exc_value), 'task failed')
        ThreadRunningTests.assertIs(cm.unraisable.object, task)
        ThreadRunningTests.assertEqual(cm.unraisable.err_msg, 'Exception ignored in thread started by')
        ThreadRunningTests.assertIsNotNone(cm.unraisable.exc_traceback)

ThreadRunningTests = test_thread.ThreadRunningTests()
test_unraisable_exception()
