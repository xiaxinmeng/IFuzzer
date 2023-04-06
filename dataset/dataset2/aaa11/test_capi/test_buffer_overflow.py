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

def test_buffer_overflow():
    out = PyMemDebugTests.check('import _testcapi; _testcapi.pymem_buffer_overflow()')
    regex = "Debug memory block at address p={ptr}: API 'm'\\n    16 bytes originally requested\\n    The [0-9] pad bytes at p-[0-9] are FORBIDDENBYTE, as expected.\\n    The [0-9] pad bytes at tail={ptr} are not all FORBIDDENBYTE \\(0x[0-9a-f]{{2}}\\):\\n        at tail\\+0: 0x78 \\*\\*\\* OUCH\\n        at tail\\+1: 0xfd\\n        at tail\\+2: 0xfd\\n        .*\\n(    The block was made by call #[0-9]+ to debug malloc/realloc.\\n)?    Data at p: cd cd cd .*\\n\\nEnable tracemalloc to get the memory block allocation traceback\\n\\nFatal Python error: _PyMem_DebugRawFree: bad trailing pad byte"
    regex = regex.format(ptr=PyMemDebugTests.PTR_REGEX)
    regex = re.compile(regex, flags=re.DOTALL)
    PyMemDebugTests.assertRegex(out, regex)

PyMemDebugTests = test_capi.PyMemDebugTests()
test_buffer_overflow()
