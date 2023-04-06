import unittest
import sys

class LogRecordTest(unittest.TestCase):
    def test_multiprocessing(self):
        import multiprocessing.queues
        del sys.modules['multiprocessing']
        import multiprocessing