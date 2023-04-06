import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_nowait():
    q = BaseQueueTestMixin.type2test(QUEUE_SIZE)
    for i in range(QUEUE_SIZE):
        q.put_nowait(1)
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Full):
        q.put_nowait(1)
    for i in range(QUEUE_SIZE):
        q.get_nowait()
    with BaseQueueTestMixin.assertRaises(BaseQueueTestMixin.queue.Empty):
        q.get_nowait()

BaseQueueTestMixin = test_queue.BaseQueueTestMixin()
test_nowait()
