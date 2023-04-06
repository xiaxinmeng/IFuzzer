from collections import namedtuple
from io import StringIO
import linecache
import sys
import unittest
import re
from test import support
from test.support import Error, captured_output, cpython_only, ALWAYS_EQ
from test.support.os_helper import TESTFN, unlink
from test.support.script_helper import assert_python_ok
import textwrap
import traceback
import sys, subprocess
from _testcapi import traceback_print
from _testcapi import exception_print
from _testcapi import exception_print
from _testcapi import exception_print
import test_traceback

def test_message_none():
    err = BaseExceptionReportingTests.get_report(Exception(None))
    BaseExceptionReportingTests.assertIn('Exception: None\n', err)
    err = BaseExceptionReportingTests.get_report(Exception('None'))
    BaseExceptionReportingTests.assertIn('Exception: None\n', err)
    err = BaseExceptionReportingTests.get_report(Exception())
    BaseExceptionReportingTests.assertIn('Exception\n', err)
    err = BaseExceptionReportingTests.get_report(Exception(''))
    BaseExceptionReportingTests.assertIn('Exception\n', err)

BaseExceptionReportingTests = test_traceback.BaseExceptionReportingTests()
test_message_none()
