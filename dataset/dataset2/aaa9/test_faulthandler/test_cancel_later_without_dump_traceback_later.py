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

def test_cancel_later_without_dump_traceback_later():
    code = dedent('\n            import faulthandler\n            faulthandler.cancel_dump_traceback_later()\n        ')
    (output, exitcode) = FaultHandlerTests.get_output(code)
    FaultHandlerTests.assertEqual(output, [])
    FaultHandlerTests.assertEqual(exitcode, 0)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_cancel_later_without_dump_traceback_later()
