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

def test_idle_process_reuse_one():
    executor = ProcessPoolExecutorTest.executor_type(4)
    executor.submit(mul, 21, 2).result()
    executor.submit(mul, 6, 7).result()
    executor.submit(mul, 3, 14).result()
    ProcessPoolExecutorTest.assertEqual(len(executor._processes), 1)
    executor.shutdown()

ProcessPoolExecutorTest = test_concurrent_futures.ProcessPoolExecutorTest()
test_idle_process_reuse_one()
