import locale
import subprocess
import sys
import textwrap
import unittest
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support import os_helper
import test_utf8_mode

def test_pyio_encoding():
    UTF8ModeTests.check_io_encoding('_pyio')

UTF8ModeTests = test_utf8_mode.UTF8ModeTests()
test_pyio_encoding()
