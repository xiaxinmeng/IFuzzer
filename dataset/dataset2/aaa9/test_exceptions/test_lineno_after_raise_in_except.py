import copy
import gc
import os
import sys
import unittest
import pickle
import weakref
import errno
from test.support import captured_stderr, check_impl_detail, cpython_only, gc_collect, no_tracing, script_helper, SuppressCrashReport
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink
from test.support.warnings_helper import check_warnings
from test import support
import marshal
import _testcapi
import _testcapi
import _testcapi
import traceback
from _testcapi import raise_memoryerror
import _testcapi
from _testcapi import raise_memoryerror
import test_exceptions

def test_lineno_after_raise_in_except():

    def in_except():
        try:
            1 / 0
        except:
            1 / 0
            pass
    PEP626Tests.lineno_after_raise(in_except, 4)

PEP626Tests = test_exceptions.PEP626Tests()
test_lineno_after_raise_in_except()
