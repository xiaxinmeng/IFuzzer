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

@unittest.skipUnless(hasattr(test_capi._testcapi, 'negative_refcount'), 'need _testcapi.negative_refcount')
def test_negative_refcount():
    code = textwrap.dedent('\n            import _testcapi\n            from test import support\n\n            with support.SuppressCrashReport():\n                _testcapi.negative_refcount()\n        ')
    (rc, out, err) = assert_python_failure('-c', code)
    CAPITest.assertRegex(err, b'_testcapimodule\\.c:[0-9]+: _Py_NegativeRefcount: Assertion failed: object has negative ref count')

CAPITest = test_capi.CAPITest()
test_negative_refcount()
