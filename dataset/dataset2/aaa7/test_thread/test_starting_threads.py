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

def test_starting_threads():
    with threading_helper.wait_threads_exit():
        for i in range(NUMTASKS):
            ThreadRunningTests.newtask()
        verbose_print('waiting for tasks to complete...')
        ThreadRunningTests.done_mutex.acquire()
        test_thread.verbose_print('all tasks done')
NUMTASKS = 10

ThreadRunningTests = test_thread.ThreadRunningTests()
ThreadRunningTests.setUp()
test_starting_threads()
