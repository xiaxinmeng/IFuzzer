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

def test_decoder():
    for (input, eof, output) in StatefulIncrementalDecoderTest.test_cases:
        d = StatefulIncrementalDecoder()
        StatefulIncrementalDecoderTest.assertEqual(d.decode(input, eof), output)
    d = StatefulIncrementalDecoder()
    StatefulIncrementalDecoderTest.assertEqual(d.decode(b'oiabcd'), '')
    StatefulIncrementalDecoderTest.assertEqual(d.decode(b'', 1), 'abcd.')

StatefulIncrementalDecoderTest = test_io.StatefulIncrementalDecoderTest()
test_decoder()
