import io
import os
import sys
import tempfile
import unittest
from test.support import os_helper

import test_winconsoleio

def test_input():
    WindowsConsoleIOTests.assertStdinRoundTrip('abc123')
    WindowsConsoleIOTests.assertStdinRoundTrip('ϼўТλФЙ')
    WindowsConsoleIOTests.assertStdinRoundTrip('A͏B ﬖ̳AA̝')

WindowsConsoleIOTests = test_winconsoleio.WindowsConsoleIOTests()
test_input()
