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

@unittest.skipIf(sys.platform == 'win32', 'SIGFPE cannot be caught on Windows')
def test_sigfpe():
    FaultHandlerTests.check_fatal_error('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler._sigfpe()\n            ', 3, 'Floating point exception')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_sigfpe()
