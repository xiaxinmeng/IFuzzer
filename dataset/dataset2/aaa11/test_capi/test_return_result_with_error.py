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

def test_return_result_with_error():
    if test_capi.Py_DEBUG:
        code = textwrap.dedent('\n                import _testcapi\n                from test import support\n\n                with support.SuppressCrashReport():\n                    _testcapi.return_result_with_error()\n            ')
        (rc, out, err) = assert_python_failure('-c', code)
        CAPITest.assertRegex(err.replace(b'\r', b''), b'Fatal Python error: _Py_CheckFunctionResult: a function returned a result with an error set\\nPython runtime state: initialized\\nValueError\\n\\nThe above exception was the direct cause of the following exception:\\n\\nSystemError: <built-in function return_result_with_error> returned a result with an error set\\n\\nCurrent thread.*:\\n  File .*, line 6 in <module>')
    else:
        with CAPITest.assertRaises(SystemError) as cm:
            test_capi._testcapi.return_result_with_error()
        CAPITest.assertRegex(str(cm.exception), 'return_result_with_error.* returned a result with an error set')

CAPITest = test_capi.CAPITest()
test_return_result_with_error()
