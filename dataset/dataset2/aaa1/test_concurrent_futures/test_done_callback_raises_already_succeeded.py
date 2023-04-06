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

def test_done_callback_raises_already_succeeded():
    with support.captured_stderr() as stderr:

        def raising_fn(callback_future):
            raise Exception('doh!')
        f = Future()
        f.set_result(5)
        f.add_done_callback(raising_fn)
        FutureTests.assertIn('exception calling callback for', stderr.getvalue())
        FutureTests.assertIn('doh!', stderr.getvalue())

FutureTests = test_concurrent_futures.FutureTests()
test_done_callback_raises_already_succeeded()
