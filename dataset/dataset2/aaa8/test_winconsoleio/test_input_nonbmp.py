import io
import os
import sys
import tempfile
import unittest
from test.support import os_helper

import test_winconsoleio

@unittest.skipIf(True, 'Handling Non-BMP characters is broken')
def test_input_nonbmp():
    WindowsConsoleIOTests.assertStdinRoundTrip('\U00100000\U0010ffff\U0010fffd')

WindowsConsoleIOTests = test_winconsoleio.WindowsConsoleIOTests()
test_input_nonbmp()
