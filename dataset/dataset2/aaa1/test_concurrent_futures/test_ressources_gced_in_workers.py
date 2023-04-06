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

@hashlib_helper.requires_hashdigest('md5')
def test_ressources_gced_in_workers():
    mgr = get_context(ProcessPoolExecutorTest.ctx).Manager()
    obj = EventfulGCObj(mgr)
    future = ProcessPoolExecutorTest.executor.submit(id, obj)
    future.result()
    ProcessPoolExecutorTest.assertTrue(obj.event.wait(timeout=1))
    obj = None
    support.gc_collect()
    mgr.shutdown()
    mgr.join()

ProcessPoolExecutorTest = test_concurrent_futures.ProcessPoolExecutorTest()
test_ressources_gced_in_workers()
