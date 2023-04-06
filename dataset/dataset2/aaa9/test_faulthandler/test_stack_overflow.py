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

@unittest.skipIf(sys.platform.startswith('openbsd'), "Issue #12868: sigaltstack() doesn't work on OpenBSD if Python is compiled with pthread")
@unittest.skipIf(not hasattr(faulthandler, '_stack_overflow'), 'need faulthandler._stack_overflow()')
def test_stack_overflow():
    FaultHandlerTests.check_fatal_error('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler._stack_overflow()\n            ', 3, '(?:Segmentation fault|Bus error)', other_regex='unable to raise a stack overflow')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_stack_overflow()
