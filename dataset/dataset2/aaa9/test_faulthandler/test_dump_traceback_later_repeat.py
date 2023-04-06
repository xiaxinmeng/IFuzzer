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

def test_dump_traceback_later_repeat():
    FaultHandlerTests.check_dump_traceback_later(repeat=True)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_dump_traceback_later_repeat()