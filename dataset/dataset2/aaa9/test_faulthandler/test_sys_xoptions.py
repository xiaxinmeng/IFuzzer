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

def test_sys_xoptions():
    code = 'import faulthandler; print(faulthandler.is_enabled())'
    args = filter(None, (sys.executable, '-E' if sys.flags.ignore_environment else '', '-X', 'faulthandler', '-c', code))
    env = os.environ.copy()
    env.pop('PYTHONFAULTHANDLER', None)
    output = subprocess.check_output(args, env=env)
    FaultHandlerTests.assertEqual(output.rstrip(), b'True')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_sys_xoptions()
