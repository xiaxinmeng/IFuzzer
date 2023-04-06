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

def test_result_with_cancel():

    def notification():
        time.sleep(1)
        f1.cancel()
    f1 = test_concurrent_futures.create_future(state=PENDING)
    t = threading.Thread(target=notification)
    t.start()
    FutureTests.assertRaises(futures.CancelledError, f1.result, timeout=support.SHORT_TIMEOUT)
    t.join()

FutureTests = test_concurrent_futures.FutureTests()
test_result_with_cancel()
