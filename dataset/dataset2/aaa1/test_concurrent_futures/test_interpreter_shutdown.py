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

def test_interpreter_shutdown():
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n            from concurrent.futures import {executor_type}\n            from time import sleep\n            from test.test_concurrent_futures import sleep_and_print\n            if __name__ == "__main__":\n                context = \'{context}\'\n                if context == "":\n                    t = {executor_type}(5)\n                else:\n                    from multiprocessing import get_context\n                    context = get_context(context)\n                    t = {executor_type}(5, mp_context=context)\n                t.submit(sleep_and_print, 1.0, "apple")\n            '.format(executor_type=ExecutorShutdownTest.executor_type.__name__, context=getattr(ExecutorShutdownTest, 'ctx', '')))
    ExecutorShutdownTest.assertFalse(err)
    ExecutorShutdownTest.assertEqual(out.strip(), b'apple')

ExecutorShutdownTest = test_concurrent_futures.ExecutorShutdownTest()
test_interpreter_shutdown()
