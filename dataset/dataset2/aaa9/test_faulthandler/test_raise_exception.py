from contextlib import contextmanager
import datetime
import faulthandler
import os
import signal
import subprocess
import sys
import sysconfig
from test import support
from test.support import os_helper
from test.support import script_helper, is_android
import tempfile
import unittest
from textwrap import dedent
import _testcapi
import test_faulthandler

@unittest.skipUnless(test_faulthandler.MS_WINDOWS, 'specific to Windows')
def test_raise_exception():
    for (exc, name) in (('EXCEPTION_ACCESS_VIOLATION', 'access violation'), ('EXCEPTION_INT_DIVIDE_BY_ZERO', 'int divide by zero'), ('EXCEPTION_STACK_OVERFLOW', 'stack overflow')):
        FaultHandlerTests.check_windows_exception(f'\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._raise_exception(faulthandler._{exc})\n                ', 3, name)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_raise_exception()
