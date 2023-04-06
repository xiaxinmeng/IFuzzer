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

def test_context_manager_shutdown():
    with futures.ProcessPoolExecutor(max_workers=5) as e:
        processes = e._processes
        ThreadPoolShutdownTest.assertEqual(list(e.map(abs, range(-5, 5))), [5, 4, 3, 2, 1, 0, 1, 2, 3, 4])
    for p in processes.values():
        p.join()

ThreadPoolShutdownTest = test_concurrent_futures.ThreadPoolShutdownTest()
test_context_manager_shutdown()
