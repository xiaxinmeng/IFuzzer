import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_negative_timeout_raises_exception():
    q = BaseQueueTestMixin.q
    q.put(1)
    with BaseQueueTestMixin.assertRaises(ValueError):
        q.get(timeout=-1)

BaseQueueTestMixin = test_queue.BaseQueueTestMixin()
test_negative_timeout_raises_exception()
