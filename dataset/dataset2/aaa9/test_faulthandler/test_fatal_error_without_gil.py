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

def test_fatal_error_without_gil():
    FaultHandlerTests.check_fatal_error("\n            import faulthandler\n            faulthandler._fatal_error(b'xyz', True)\n            ", 2, 'xyz', func='faulthandler_fatal_error_py', py_fatal_error=True)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_fatal_error_without_gil()
