import test.support
from test.support import threading_helper
from test.support import verbose, cpython_only
from test.support.import_helper import import_module
from test.support.script_helper import assert_python_ok, assert_python_failure
import random
import sys
import _thread
import threading
import time
import unittest
import weakref
import os
import subprocess
import signal
import textwrap
from unittest import mock
from test import lock_tests
from test import support
import _testcapi
import test_threading

def test_init_immutable_default_args():
    timer1 = threading.Timer(0.01, TimerTests._callback_spy)
    timer1.start()
    TimerTests.callback_event.wait()
    timer1.args.append('blah')
    timer1.kwargs['foo'] = 'bar'
    TimerTests.callback_event.clear()
    timer2 = threading.Timer(0.01, TimerTests._callback_spy)
    timer2.start()
    TimerTests.callback_event.wait()
    TimerTests.assertEqual(len(TimerTests.callback_args), 2)
    TimerTests.assertEqual(TimerTests.callback_args, [((), {}), ((), {})])
    timer1.join()
    timer2.join()

TimerTests = test_threading.TimerTests()
test_init_immutable_default_args()
