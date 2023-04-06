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

def test_barrier():
    with threading_helper.wait_threads_exit():
        BarrierTest.bar = test_thread.Barrier(NUMTASKS)
        BarrierTest.running = NUMTASKS
        for i in range(NUMTASKS):
            thread.start_new_thread(BarrierTest.task2, (i,))
        test_thread.verbose_print('waiting for tasks to end')
        BarrierTest.done_mutex.acquire()
        test_thread.verbose_print('tasks done')
NUMTASKS = 10
BarrierTest = test_thread.BarrierTest()
test_barrier()
