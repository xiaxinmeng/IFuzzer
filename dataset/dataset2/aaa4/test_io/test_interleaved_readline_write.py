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

def test_interleaved_readline_write():
    with BufferedRandomTest.BytesIO(b'ab\ncdef\ng\n') as raw:
        with BufferedRandomTest.tp(raw) as f:
            f.write(b'1')
            BufferedRandomTest.assertEqual(f.readline(), b'b\n')
            f.write(b'2')
            BufferedRandomTest.assertEqual(f.readline(), b'def\n')
            f.write(b'3')
            BufferedRandomTest.assertEqual(f.readline(), b'\n')
            f.flush()
            BufferedRandomTest.assertEqual(raw.getvalue(), b'1b\n2def\n3\n')

BufferedRandomTest = test_io.BufferedRandomTest()
test_interleaved_readline_write()
