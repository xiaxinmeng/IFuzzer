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

def test_stderr_None():
    with FaultHandlerTests.check_stderr_none():
        faulthandler.enable()
    with FaultHandlerTests.check_stderr_none():
        faulthandler.dump_traceback()
    with FaultHandlerTests.check_stderr_none():
        faulthandler.dump_traceback_later(0.001)
    if hasattr(faulthandler, 'register'):
        with FaultHandlerTests.check_stderr_none():
            faulthandler.register(signal.SIGUSR1)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_stderr_None()
