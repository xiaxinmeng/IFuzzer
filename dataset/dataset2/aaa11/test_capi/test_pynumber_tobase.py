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

def test_pynumber_tobase():
    from _testcapi import pynumber_tobase
    CAPITest.assertEqual(pynumber_tobase(123, 2), '0b1111011')
    CAPITest.assertEqual(pynumber_tobase(123, 8), '0o173')
    CAPITest.assertEqual(pynumber_tobase(123, 10), '123')
    CAPITest.assertEqual(pynumber_tobase(123, 16), '0x7b')
    CAPITest.assertEqual(pynumber_tobase(-123, 2), '-0b1111011')
    CAPITest.assertEqual(pynumber_tobase(-123, 8), '-0o173')
    CAPITest.assertEqual(pynumber_tobase(-123, 10), '-123')
    CAPITest.assertEqual(pynumber_tobase(-123, 16), '-0x7b')
    CAPITest.assertRaises(TypeError, pynumber_tobase, 123.0, 10)
    CAPITest.assertRaises(TypeError, pynumber_tobase, '123', 10)
    CAPITest.assertRaises(SystemError, pynumber_tobase, 123, 0)

CAPITest = test_capi.CAPITest()
test_pynumber_tobase()
