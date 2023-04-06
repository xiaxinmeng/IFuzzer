import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_references():

    class C:
        pass
    N = 20
    q = BaseSimpleQueueTest.q
    for i in range(N):
        q.put(C())
    for i in range(N):
        wr = weakref.ref(q.get())
        BaseSimpleQueueTest.assertIsNone(wr())

BaseSimpleQueueTest = test_queue.BaseSimpleQueueTest()
test_references()
