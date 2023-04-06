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
def test_subprocess_fork_exec():

    class Z(object):

        def __len__(CAPITest):
            return 1
    CAPITest.assertRaises(TypeError, _posixsubprocess.fork_exec, Z(), [b'1'], 3, (1, 2), 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

CAPITest = test_capi.CAPITest()
test_subprocess_fork_exec()
