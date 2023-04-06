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

def test_initializer():
    with InitializerMixin._assert_logged('ValueError: error in initializer'):
        try:
            future = InitializerMixin.executor.submit(get_init_status)
        except BrokenExecutor:
            pass
        else:
            with InitializerMixin.assertRaises(BrokenExecutor):
                future.result()
        t1 = time.monotonic()
        while not InitializerMixin.executor._broken:
            if time.monotonic() - t1 > 5:
                InitializerMixin.fail('executor not broken after 5 s.')
            time.sleep(0.01)
        with InitializerMixin.assertRaises(BrokenExecutor):
            InitializerMixin.executor.submit(get_init_status)

InitializerMixin = test_concurrent_futures.InitializerMixin()

test_initializer()
