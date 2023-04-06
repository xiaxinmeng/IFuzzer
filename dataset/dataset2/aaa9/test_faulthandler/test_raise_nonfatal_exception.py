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
def test_raise_nonfatal_exception():
    for exc in (0, 878082192, 1073741824, 1073745920, 1879048192, 2147483647):
        (output, exitcode) = FaultHandlerTests.get_output(f'\n                import faulthandler\n                faulthandler.enable()\n                faulthandler._raise_exception(0x{exc:x})\n                ')
        FaultHandlerTests.assertEqual(output, [])
        FaultHandlerTests.assertIn(exitcode, (exc, exc & ~268435456))

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_raise_nonfatal_exception()
