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

def test_read1_arbitrary():
    rawio = BufferedReaderTest.MockRawIO((b'abc', b'd', b'efg'))
    bufio = BufferedReaderTest.tp(rawio)
    BufferedReaderTest.assertEqual(b'a', bufio.read(1))
    BufferedReaderTest.assertEqual(b'bc', bufio.read1())
    BufferedReaderTest.assertEqual(b'd', bufio.read1())
    BufferedReaderTest.assertEqual(b'efg', bufio.read1(-1))
    BufferedReaderTest.assertEqual(rawio._reads, 3)
    BufferedReaderTest.assertEqual(b'', bufio.read1())
    BufferedReaderTest.assertEqual(rawio._reads, 4)

BufferedReaderTest = test_io.BufferedReaderTest()
test_read1_arbitrary()
