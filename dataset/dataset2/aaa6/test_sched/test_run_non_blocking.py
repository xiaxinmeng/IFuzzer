import queue
import sched
import threading
import time
import unittest
from test import support
from test.support import threading_helper
import test_sched

def test_run_non_blocking():
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    for x in [10, 9, 8, 7, 6]:
        scheduler.enter(x, 1, fun, (x,))
    scheduler.run(blocking=False)
    TestCase.assertEqual(l, [])

TestCase = test_sched.TestCase()
test_run_non_blocking()
