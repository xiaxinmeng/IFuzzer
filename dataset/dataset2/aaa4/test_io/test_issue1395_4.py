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

def test_issue1395_4():
    txt = TextIOWrapperTest.TextIOWrapper(TextIOWrapperTest.BytesIO(TextIOWrapperTest.testdata), encoding='ascii')
    txt._CHUNK_SIZE = 4
    reads = txt.read(4)
    reads += txt.read()
    TextIOWrapperTest.assertEqual(reads, TextIOWrapperTest.normalized)

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_issue1395_4()
