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

@support.cpython_only
def test_no_stale_references():
    my_object = test_concurrent_futures.MyObject()
    my_object_collected = threading.Event()
    my_object_callback = weakref.ref(my_object, lambda obj: my_object_collected.set())
    ExecutorTest.executor.submit(my_object.my_method)
    del my_object
    collected = my_object_collected.wait(timeout=support.SHORT_TIMEOUT)
    ExecutorTest.assertTrue(collected, 'Stale reference not collected within timeout.')

ExecutorTest = test_concurrent_futures.ExecutorTest()
test_no_stale_references()
