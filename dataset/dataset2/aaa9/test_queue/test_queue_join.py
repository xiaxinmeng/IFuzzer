import itertools
import random
import threading
import time
import unittest
import weakref
from test.support import import_helper
from test.support import threading_helper
import test_queue

def test_queue_join():
    q = BaseQueueTestMixin.type2test()
    BaseQueueTestMixin.queue_join_test(q)
    BaseQueueTestMixin.queue_join_test(q)
    try:
        q.task_done()
    except ValueError:
        pass
    else:
        BaseQueueTestMixin.fail('Did not detect task count going negative')

BaseQueueTestMixin = test_queue.BaseQueueTestMixin()
test_queue_join()
