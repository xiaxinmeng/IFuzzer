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

def test_truncate_after_read_or_write():
    raw = BufferedRandomTest.BytesIO(b'A' * 10)
    bufio = BufferedRandomTest.tp(raw, 100)
    BufferedRandomTest.assertEqual(bufio.read(2), b'AA')
    BufferedRandomTest.assertEqual(bufio.truncate(), 2)
    BufferedRandomTest.assertEqual(bufio.write(b'BB'), 2)
    BufferedRandomTest.assertEqual(bufio.truncate(), 4)

BufferedRandomTest = test_io.BufferedRandomTest()
test_truncate_after_read_or_write()
