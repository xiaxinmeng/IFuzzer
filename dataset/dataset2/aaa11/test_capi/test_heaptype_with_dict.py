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

def test_heaptype_with_dict():
    inst = test_capi._testcapi.HeapCTypeWithDict()
    inst.foo = 42
    CAPITest.assertEqual(inst.foo, 42)
    CAPITest.assertEqual(inst.dictobj, inst.__dict__)
    CAPITest.assertEqual(inst.dictobj, {'foo': 42})
    inst = test_capi._testcapi.HeapCTypeWithDict()
    CAPITest.assertEqual({}, inst.__dict__)

CAPITest = test_capi.CAPITest()
test_heaptype_with_dict()
