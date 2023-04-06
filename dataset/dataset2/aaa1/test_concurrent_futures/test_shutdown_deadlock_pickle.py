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

def test_shutdown_deadlock_pickle():
    ExecutorDeadlockTest.executor.shutdown(wait=True)
    with ExecutorDeadlockTest.executor_type(max_workers=2, mp_context=get_context(ExecutorDeadlockTest.ctx)) as executor:
        ExecutorDeadlockTest.executor = executor
        executor.submit(id, 42).result()
        executor_manager = executor._executor_manager_thread
        f = executor.submit(id, ErrorAtPickle())
        executor.shutdown(wait=False)
        with ExecutorDeadlockTest.assertRaises(PicklingError):
            f.result()
    executor_manager.join()

ExecutorDeadlockTest = test_concurrent_futures.ExecutorDeadlockTest()
test_shutdown_deadlock_pickle()
