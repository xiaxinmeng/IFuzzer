import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_shrinking_queue():
    q = BaseQueueTestMixin.type2test(3)
    q.put(1)
    q.put(2)
    q.put(3)
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Full):
        q.put_nowait(4)
    BaseQueueTestMixin.assertEqual(q.qsize(), 3)
    q.maxsize = 2
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Full):
        q.put_nowait(4)

BaseQueueTestMixin = test_queue.BaseQueueTestMixin()
test_shrinking_queue()
