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
def test_dump_traceback_fd():
    with tempfile.TemporaryFile('wb+') as fp:
        FaultHandlerTests.check_dump_traceback(fd=fp.fileno())

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_dump_traceback_fd()
