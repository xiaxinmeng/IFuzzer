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

def test_is_enabled():
    orig_stderr = sys.stderr
    try:
        sys.stderr = sys.__stderr__
        was_enabled = faulthandler.is_enabled()
        try:
            faulthandler.enable()
            FaultHandlerTests.assertTrue(faulthandler.is_enabled())
            faulthandler.disable()
            FaultHandlerTests.assertFalse(faulthandler.is_enabled())
        finally:
            if was_enabled:
                faulthandler.enable()
            else:
                faulthandler.disable()
    finally:
        sys.stderr = orig_stderr

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_is_enabled()
