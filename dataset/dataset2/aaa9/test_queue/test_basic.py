import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_basic():
    q = BaseQueueTestMixin.q
    BaseQueueTestMixin.assertTrue(q.empty())
    BaseQueueTestMixin.assertEqual(q.qsize(), 0)
    q.put(1)
    BaseQueueTestMixin.assertFalse(q.empty())
    BaseQueueTestMixin.assertEqual(q.qsize(), 1)
    q.put(2)
    q.put_nowait(3)
    q.put(4)
    BaseQueueTestMixin.assertFalse(q.empty())
    BaseQueueTestMixin.assertEqual(q.qsize(), 4)
    BaseQueueTestMixin.assertEqual(q.get(), 1)
    BaseQueueTestMixin.assertEqual(q.qsize(), 3)
    BaseQueueTestMixin.assertEqual(q.get_nowait(), 2)
    BaseQueueTestMixin.assertEqual(q.qsize(), 2)
    BaseQueueTestMixin.assertEqual(q.get(block=False), 3)
    BaseQueueTestMixin.assertFalse(q.empty())
    BaseQueueTestMixin.assertEqual(q.qsize(), 1)
    BaseQueueTestMixin.assertEqual(q.get(timeout=0.1), 4)
    BaseQueueTestMixin.assertTrue(q.empty())
    BaseQueueTestMixin.assertEqual(q.qsize(), 0)
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Empty):
        q.get(block=False)
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Empty):
        q.get(timeout=0.001)
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Empty):
        q.get_nowait()
    BaseQueueTestMixin.assertTrue(q.empty())
    BaseQueueTestMixin.assertEqual(q.qsize(), 0)

BaseQueueTestMixin = test_queue.BaseQueueTestMixin()
BaseQueueTestMixin.setUp()
test_basic()
