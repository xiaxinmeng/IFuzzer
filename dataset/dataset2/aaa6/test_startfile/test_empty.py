import unittest
from test import support
from test.support import os_helper
import os
import platform
import sys
from os import path
import test_startfile

@unittest.skipIf(platform.win32_is_iot(), 'starting files is not supported on Windows IoT Core or nanoserver')
def test_empty():
    with os_helper.change_cwd(path.dirname(sys.executable)):
        empty = path.join(path.dirname(__file__), 'empty.vbs')
        startfile(empty)
        startfile(empty, 'open')

TestCase = test_startfile.TestCase()
test_empty()
