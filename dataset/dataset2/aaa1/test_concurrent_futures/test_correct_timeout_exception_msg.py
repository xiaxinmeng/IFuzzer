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

def test_correct_timeout_exception_msg():
    futures_list = [test_concurrent_futures.CANCELLED_AND_NOTIFIED_FUTURE, test_concurrent_futures.PENDING_FUTURE, test_concurrent_futures.RUNNING_FUTURE, test_concurrent_futures.SUCCESSFUL_FUTURE]
    with AsCompletedTests.assertRaises(futures.TimeoutError) as cm:
        list(futures.as_completed(futures_list, timeout=0))
    AsCompletedTests.assertEqual(str(cm.exception), '2 (of 4) futures unfinished')

AsCompletedTests = test_concurrent_futures.AsCompletedTests()

test_correct_timeout_exception_msg()
