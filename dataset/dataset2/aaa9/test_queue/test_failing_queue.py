import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_failing_queue():
    q = FailingQueueTest.FailingQueue(QUEUE_SIZE)
    FailingQueueTest.failing_queue_test(q)
    FailingQueueTest.failing_queue_test(q)

FailingQueueTest = test_queue.FailingQueueTest()
FailingQueueTest.setUp()
test_failing_queue()
