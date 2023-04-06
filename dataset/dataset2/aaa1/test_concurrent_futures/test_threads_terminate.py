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

def test_threads_terminate():

    def acquire_lock(lock):
        lock.acquire()
    sem = threading.Semaphore(0)
    for i in range(3):
        ThreadPoolShutdownTest.executor.submit(acquire_lock, sem)
    ThreadPoolShutdownTest.assertEqual(len(ThreadPoolShutdownTest.executor._threads), 3)
    for i in range(3):
        sem.release()
    ThreadPoolShutdownTest.executor.shutdown()
    for t in ThreadPoolShutdownTest.executor._threads:
        t.join()

ThreadPoolShutdownTest = test_concurrent_futures.ThreadPoolShutdownTest()
test_threads_terminate()
