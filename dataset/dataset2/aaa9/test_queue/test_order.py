import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_order():
    q = BaseSimpleQueueTest.q
    inputs = list(range(100))
    results = BaseSimpleQueueTest.run_threads(1, 1, q, inputs, BaseSimpleQueueTest.feed, BaseSimpleQueueTest.consume)
    BaseSimpleQueueTest.assertEqual(results, inputs)

BaseSimpleQueueTest = test_queue.BaseSimpleQueueTest()
test_order()
