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

@test_faulthandler.skip_segfault_on_android
def test_sigsegv():
    FaultHandlerTests.check_fatal_error('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler._sigsegv()\n            ', 3, 'Segmentation fault')

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_sigsegv()
