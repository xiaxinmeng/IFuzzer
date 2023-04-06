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

@unittest.skipIf(sys.platform == 'win32', "subprocess doesn't support pass_fds on Windows")
@unittest.skipIf(test_faulthandler.UB_SANITIZER or test_faulthandler.MEMORY_SANITIZER, 'sanitizer builds change crashing process output.')
@test_faulthandler.skip_segfault_on_android
def test_enable_fd():
    with tempfile.TemporaryFile('wb+') as fp:
        fd = fp.fileno()
        FaultHandlerTests.check_fatal_error('\n                import faulthandler\n                import sys\n                faulthandler.enable(%s)\n                faulthandler._sigsegv()\n                ' % fd, 4, 'Segmentation fault', fd=fd)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_enable_fd()
