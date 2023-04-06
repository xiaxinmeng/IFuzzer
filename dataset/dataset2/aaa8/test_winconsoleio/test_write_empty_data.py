import io
import os
import sys
import tempfile
import unittest
from test.support import os_helper

import test_winconsoleio

def test_write_empty_data():
    with ConIO('CONOUT$', 'w') as f:
        WindowsConsoleIOTests.assertEqual(f.write(b''), 0)

WindowsConsoleIOTests = test_winconsoleio.WindowsConsoleIOTests()
test_write_empty_data()
