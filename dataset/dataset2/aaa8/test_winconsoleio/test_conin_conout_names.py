import io
import os
import sys
import tempfile
import unittest
from test.support import os_helper

import test_winconsoleio

@unittest.skipIf(sys.getwindowsversion()[:2] <= (6, 1), 'test does not work on Windows 7 and earlier')
def test_conin_conout_names():
    f = open('\\\\.\\conin$', 'rb', buffering=0)
    WindowsConsoleIOTests.assertIsInstance(f, ConIO)
    f.close()
    f = open('//?/conout$', 'wb', buffering=0)
    WindowsConsoleIOTests.assertIsInstance(f, ConIO)
    f.close()

WindowsConsoleIOTests = test_winconsoleio.WindowsConsoleIOTests()
test_conin_conout_names()
