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

def test_subclass_of_heap_gc_ctype_with_tpdealloc_decrefs_once():

    class HeapGcCTypeSubclass(test_capi._testcapi.HeapGcCType):

        def __init__(CAPITest):
            CAPITest.value2 = 20
            super().__init__()
    subclass_instance = HeapGcCTypeSubclass()
    type_refcnt = sys.getrefcount(HeapGcCTypeSubclass)
    CAPITest.assertEqual(subclass_instance.value, 10)
    CAPITest.assertEqual(subclass_instance.value2, 20)
    del subclass_instance
    CAPITest.assertEqual(type_refcnt - 1, sys.getrefcount(HeapGcCTypeSubclass))

CAPITest = test_capi.CAPITest()
test_subclass_of_heap_gc_ctype_with_tpdealloc_decrefs_once()
