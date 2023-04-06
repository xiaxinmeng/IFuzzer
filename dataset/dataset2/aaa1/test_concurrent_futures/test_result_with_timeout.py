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

def test_result_with_timeout():
    FutureTests.assertRaises(futures.TimeoutError, test_concurrent_futures.PENDING_FUTURE.result, timeout=0)
    FutureTests.assertRaises(futures.TimeoutError, test_concurrent_futures.RUNNING_FUTURE.result, timeout=0)
    FutureTests.assertRaises(futures.CancelledError, test_concurrent_futures.CANCELLED_FUTURE.result, timeout=0)
    FutureTests.assertRaises(futures.CancelledError, test_concurrent_futures.CANCELLED_AND_NOTIFIED_FUTURE.result, timeout=0)
    FutureTests.assertRaises(OSError, test_concurrent_futures.EXCEPTION_FUTURE.result, timeout=0)
    FutureTests.assertEqual(test_concurrent_futures.SUCCESSFUL_FUTURE.result(timeout=0), 42)

FutureTests = test_concurrent_futures.FutureTests()
test_result_with_timeout()
