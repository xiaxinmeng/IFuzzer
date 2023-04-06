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
def test_disable_windows_exc_handler():
    code = dedent('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler.disable()\n            code = faulthandler._EXCEPTION_ACCESS_VIOLATION\n            faulthandler._raise_exception(code)\n        ')
    (output, exitcode) = FaultHandlerTests.get_output(code)
    FaultHandlerTests.assertEqual(output, [])
    FaultHandlerTests.assertEqual(exitcode, 3221225477)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_disable_windows_exc_handler()
