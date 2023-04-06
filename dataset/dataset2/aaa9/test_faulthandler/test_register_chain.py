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

def test_register_chain():
    FaultHandlerTests.check_register(chain=True)

FaultHandlerTests = test_faulthandler.FaultHandlerTests()
test_register_chain()
