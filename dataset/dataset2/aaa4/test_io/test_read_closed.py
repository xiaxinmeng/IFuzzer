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

def test_read_closed():
    with IOTest.open(os_helper.TESTFN, 'w') as f:
        f.write('egg\n')
    with IOTest.open(os_helper.TESTFN, 'r') as f:
        file = IOTest.open(f.fileno(), 'r', closefd=False)
        IOTest.assertEqual(file.read(), 'egg\n')
        file.seek(0)
        file.close()
        IOTest.assertRaises(ValueError, file.read)
    with IOTest.open(os_helper.TESTFN, 'rb') as f:
        file = IOTest.open(f.fileno(), 'rb', closefd=False)
        IOTest.assertEqual(file.read()[:3], b'egg')
        file.close()
        IOTest.assertRaises(ValueError, file.readinto, bytearray(1))

IOTest = test_io.IOTest()
test_read_closed()
