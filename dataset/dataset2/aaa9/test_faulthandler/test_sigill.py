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

@unittest.skipIf(_testcapi is None, 'need _testcapi')
@unittest.skipUnless(hasattr(signal, 'SIGILL'), 'need signal.SIGILL')
@test_faulthandler.skip_segfault_on_android
def test_sigill():
    FaultHandlerTests.check_fatal_error('\n            import faulthandler\n            import signal\n\n            faulthandler.enable()\n            signal.raise_signal(signal.SIGILL)\n            ', 5, 'Illegal instruction')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_sigill()
