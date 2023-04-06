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

def test_isatty():

    class SelectableIsAtty(MockRawIO):

        def __init__(BufferedRWPairTest, isatty):
            MockRawIO.__init__(BufferedRWPairTest)
            BufferedRWPairTest._isatty = isatty

        def isatty(BufferedRWPairTest):
            return BufferedRWPairTest._isatty
    pair = BufferedRWPairTest.tp(SelectableIsAtty(False), SelectableIsAtty(False))
    BufferedRWPairTest.assertFalse(pair.isatty())
    pair = BufferedRWPairTest.tp(SelectableIsAtty(True), SelectableIsAtty(False))
    BufferedRWPairTest.assertTrue(pair.isatty())
    pair = BufferedRWPairTest.tp(SelectableIsAtty(False), SelectableIsAtty(True))
    BufferedRWPairTest.assertTrue(pair.isatty())
    pair = BufferedRWPairTest.tp(SelectableIsAtty(True), SelectableIsAtty(True))
    BufferedRWPairTest.assertTrue(pair.isatty())

BufferedRWPairTest = test_io.BufferedRWPairTest()
test_isatty()