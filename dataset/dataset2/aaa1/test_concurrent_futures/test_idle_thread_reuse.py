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

def test_idle_thread_reuse():
    executor = ThreadPoolExecutorTest.executor_type()
    executor.submit(test_concurrent_futures.mul, 21, 2).result()
    executor.submit(test_concurrent_futures.mul, 6, 7).result()
    executor.submit(test_concurrent_futures.mul, 3, 14).result()
    ThreadPoolExecutorTest.assertEqual(len(executor._threads), 1)
    executor.shutdown(wait=True)

ThreadPoolExecutorTest = test_concurrent_futures.ThreadPoolExecutorTest()
test_idle_thread_reuse()
