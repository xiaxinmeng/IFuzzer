import queue
import sched
import threading
import time
import unittest
from test import support
from test.support import threading_helper
import test_sched

def test_cancel_correct_event():
    events = []
    scheduler = sched.scheduler()
    scheduler.enterabs(1, 1, events.append, ('a',))
    b = scheduler.enterabs(1, 1, events.append, ('b',))
    scheduler.enterabs(1, 1, events.append, ('c',))
    scheduler.cancel(b)
    scheduler.run()
    TestCase.assertEqual(events, ['a', 'c'])

TestCase = test_sched.TestCase()
test_cancel_correct_event()
