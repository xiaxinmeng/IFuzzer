import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_is_default():
    CSimpleQueueTest.assertIs(CSimpleQueueTest.type2test, CSimpleQueueTest.queue.SimpleQueue)
    CSimpleQueueTest.assertIs(CSimpleQueueTest.type2test, CSimpleQueueTest.queue.SimpleQueue)

CSimpleQueueTest = test_queue.CSimpleQueueTest()
CSimpleQueueTest.setUp()
test_is_default()
