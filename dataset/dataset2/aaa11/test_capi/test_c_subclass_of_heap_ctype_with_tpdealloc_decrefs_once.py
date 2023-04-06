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

def test_c_subclass_of_heap_ctype_with_tpdealloc_decrefs_once():
    subclass_instance = test_capi._testcapi.HeapCTypeSubclass()
    type_refcnt = sys.getrefcount(test_capi._testcapi.HeapCTypeSubclass)
    CAPITest.assertEqual(subclass_instance.value, 10)
    CAPITest.assertEqual(subclass_instance.value2, 20)
    del subclass_instance
    CAPITest.assertEqual(type_refcnt - 1, sys.getrefcount(test_capi._testcapi.HeapCTypeSubclass))

CAPITest = test_capi.CAPITest()
test_c_subclass_of_heap_ctype_with_tpdealloc_decrefs_once()
