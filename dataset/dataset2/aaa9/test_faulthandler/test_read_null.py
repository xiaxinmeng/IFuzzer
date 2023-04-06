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

@unittest.skipIf(sys.platform.startswith('aix'), 'the first page of memory is a mapped read-only on AIX')
def test_read_null():
    if not test_faulthandler.MS_WINDOWS:
        FaultHandlerTests.check_fatal_error('\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._read_null()\n                ', 3, '(?:Segmentation fault|Bus error|Illegal instruction)')
    else:
        FaultHandlerTests.check_windows_exception('\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._read_null()\n                ', 3, 'access violation')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_read_null()
