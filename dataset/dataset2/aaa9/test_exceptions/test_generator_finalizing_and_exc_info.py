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

def test_generator_finalizing_and_exc_info():

    def simple_gen():
        yield 1

    def run_gen():
        gen = simple_gen()
        try:
            raise RuntimeError
        except RuntimeError:
            return next(gen)
    run_gen()
    gc_collect()
    ExceptionTests.assertEqual(sys.exc_info(), (None, None, None))

ExceptionTests = test_exceptions.ExceptionTests()
test_generator_finalizing_and_exc_info()
