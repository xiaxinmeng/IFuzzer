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

def test_old_threading_api():
    t = threading.Thread()
    t.isDaemon()
    t.setDaemon(True)
    t.getName()
    t.setName('name')
    e = threading.Event()
    e.isSet()
    threading.activeCount()

ThreadTests = test_threading.ThreadTests()
test_old_threading_api()
