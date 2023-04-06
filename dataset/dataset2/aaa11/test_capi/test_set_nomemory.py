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

def test_set_nomemory():
    code = "if 1:\n            import _testcapi\n\n            class C(): pass\n\n            # The first loop tests both functions and that remove_mem_hooks()\n            # can be called twice in a row. The second loop checks a call to\n            # set_nomemory() after a call to remove_mem_hooks(). The third\n            # loop checks the start and stop arguments of set_nomemory().\n            for outer_cnt in range(1, 4):\n                start = 10 * outer_cnt\n                for j in range(100):\n                    if j == 0:\n                        if outer_cnt != 3:\n                            _testcapi.set_nomemory(start)\n                        else:\n                            _testcapi.set_nomemory(start, start + 1)\n                    try:\n                        C()\n                    except MemoryError as e:\n                        if outer_cnt != 3:\n                            _testcapi.remove_mem_hooks()\n                        print('MemoryError', outer_cnt, j)\n                        _testcapi.remove_mem_hooks()\n                        break\n        "
    (rc, out, err) = assert_python_ok('-c', code)
    CAPITest.assertIn(b'MemoryError 1 10', out)
    CAPITest.assertIn(b'MemoryError 2 20', out)
    CAPITest.assertIn(b'MemoryError 3 30', out)

CAPITest = test_capi.CAPITest()
test_set_nomemory()
