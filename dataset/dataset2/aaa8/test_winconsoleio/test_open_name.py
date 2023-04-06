import io
import os
import sys
import tempfile
import unittest
from test.support import os_helper

import test_winconsoleio

def test_open_name():
    WindowsConsoleIOTests.assertRaises(ValueError, ConIO, sys.executable)
    f = ConIO('CON')
    WindowsConsoleIOTests.assertTrue(f.readable())
    WindowsConsoleIOTests.assertFalse(f.writable())
    WindowsConsoleIOTests.assertIsNotNone(f.fileno())
    f.close()
    f.close()
    f = ConIO('CONIN$')
    WindowsConsoleIOTests.assertTrue(f.readable())
    WindowsConsoleIOTests.assertFalse(f.writable())
    WindowsConsoleIOTests.assertIsNotNone(f.fileno())
    f.close()
    f.close()
    f = ConIO('CONOUT$', 'w')
    WindowsConsoleIOTests.assertFalse(f.readable())
    WindowsConsoleIOTests.assertTrue(f.writable())
    WindowsConsoleIOTests.assertIsNotNone(f.fileno())
    f.close()
    f.close()
    f = open('C:/con', 'rb', buffering=0)
    WindowsConsoleIOTests.assertIsInstance(f, ConIO)
    f.close()

WindowsConsoleIOTests = test_winconsoleio.WindowsConsoleIOTests()
test_open_name()
