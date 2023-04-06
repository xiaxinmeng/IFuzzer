import abc
import array
import errno
import locale
import os
import pickle
import random
import signal
import sys
import sysconfig
import textwrap
import threading
import time
import unittest
import warnings
import weakref
from collections import deque, UserList
from itertools import cycle, count
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure, run_python_until_end
from test.support import import_helper
from test.support import os_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.os_helper import FakePath
import codecs
import io
import _pyio as pyio
import ctypes
import _testcapi
import test_io

def test_truncate():
    BufferedWriterTest.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with BufferedWriterTest.open(os_helper.TESTFN, BufferedWriterTest.write_mode, buffering=0) as raw:
        bufio = BufferedWriterTest.tp(raw, 8)
        bufio.write(b'abcdef')
        BufferedWriterTest.assertEqual(bufio.truncate(3), 3)
        BufferedWriterTest.assertEqual(bufio.tell(), 6)
    with BufferedWriterTest.open(os_helper.TESTFN, 'rb', buffering=0) as f:
        BufferedWriterTest.assertEqual(f.read(), b'abc')

BufferedWriterTest = test_io.BufferedWriterTest()
test_truncate()
