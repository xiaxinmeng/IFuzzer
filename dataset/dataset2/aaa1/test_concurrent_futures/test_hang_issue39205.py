from test import support
from test.support import import_helper
from test.support import threading_helper
from test.support import hashlib_helper
from test.support.script_helper import assert_python_ok
import contextlib
import itertools
import logging
from logging.handlers import QueueHandler
import os
import queue
import sys
import threading
import time
import unittest
import weakref
from pickle import PicklingError
from concurrent import futures
from concurrent.futures._base import PENDING, RUNNING, CANCELLED, CANCELLED_AND_NOTIFIED, FINISHED, Future, BrokenExecutor
from concurrent.futures.process import BrokenProcessPool
from multiprocessing import get_context
import multiprocessing.process
import multiprocessing.util
import faulthandler
import io
from pickle import PicklingError
from pickle import UnpicklingError
import faulthandler
from tempfile import TemporaryFile
import test_concurrent_futures

def test_hang_issue39205():
    """shutdown(wait=False) doesn't hang at exit with running futures.

        See https://bugs.python.org/issue39205.
        """
    if ExecutorShutdownTest.executor_type == futures.ProcessPoolExecutor:
        raise unittest.SkipTest('Hangs due to https://bugs.python.org/issue39205')
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            from concurrent.futures import {executor_type}\n            from test.test_concurrent_futures import sleep_and_print\n            if __name__ == "__main__":\n                t = {executor_type}(max_workers=3)\n                t.submit(sleep_and_print, 1.0, "apple")\n                t.shutdown(wait=False)\n            '.format(executor_type=ExecutorShutdownTest.executor_type.__name__))
    ExecutorShutdownTest.assertFalse(err)
    ExecutorShutdownTest.assertEqual(out.strip(), b'apple')

ExecutorShutdownTest = test_concurrent_futures.ExecutorShutdownTest()
test_hang_issue39205()
