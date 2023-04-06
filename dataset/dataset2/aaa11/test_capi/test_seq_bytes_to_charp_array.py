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

@unittest.skipUnless(_posixsubprocess, '_posixsubprocess required for this test.')
def test_seq_bytes_to_charp_array():

    class Z(object):

        def __len__(CAPITest):
            return 1
    CAPITest.assertRaises(TypeError, _posixsubprocess.fork_exec, 1, Z(), 3, (1, 2), 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

    class Z(object):

        def __len__(CAPITest):
            return sys.maxsize

        def __getitem__(CAPITest, i):
            return b'x'
    CAPITest.assertRaises(MemoryError, _posixsubprocess.fork_exec, 1, Z(), 3, (1, 2), 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

CAPITest = test_capi.CAPITest()
test_seq_bytes_to_charp_array()
