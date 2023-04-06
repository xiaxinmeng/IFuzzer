from collections import OrderedDict
import os
import pickle
import random
import re
import subprocess
import sys
import textwrap
import threading
import time
import unittest
import weakref
import importlib.machinery
import importlib.util
from test import support
from test.support import MISSING_C_DOCSTRINGS
from test.support import import_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_failure, assert_python_ok
import _posixsubprocess
import _testinternalcapi
from _testcapi import MyList
from _testcapi import MyList
from _testcapi import pynumber_tobase
import builtins
import binascii
import test_capi

def test_no_FatalError_infinite_loop():
    with support.SuppressCrashReport():
        p = subprocess.Popen([sys.executable, '-c', 'import _testcapi;_testcapi.crash_no_current_thread()'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()
    CAPITest.assertEqual(out, b'')
    CAPITest.assertTrue(err.rstrip().startswith(b'Fatal Python error: PyThreadState_Get: the function must be called with the GIL held, but the GIL is released (the current Python thread state is NULL)'), err)

CAPITest = test_capi.CAPITest()
test_no_FatalError_infinite_loop()
