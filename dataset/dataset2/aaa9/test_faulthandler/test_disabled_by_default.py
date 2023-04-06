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

def test_disabled_by_default():
    code = 'import faulthandler; print(faulthandler.is_enabled())'
    args = (sys.executable, '-E', '-c', code)
    output = subprocess.check_output(args)
    FaultHandlerTests.assertEqual(output.rstrip(), b'False')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_disabled_by_default()
