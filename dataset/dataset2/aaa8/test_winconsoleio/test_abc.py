import io
import os
import sys
import tempfile
import unittest
from test.support import os_helper
import test_winconsoleio

def test_abc():
    WindowsConsoleIOTests.assertTrue(issubclass(ConIO, io.RawIOBase))
    WindowsConsoleIOTests.assertFalse(issubclass(ConIO, io.BufferedIOBase))
    WindowsConsoleIOTests.assertFalse(issubclass(ConIO, io.TextIOBase))

WindowsConsoleIOTests = test_winconsoleio.WindowsConsoleIOTests()
test_abc()
