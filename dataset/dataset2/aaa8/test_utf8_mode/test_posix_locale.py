import locale
import subprocess
import sys
import textwrap
import unittest
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support import os_helper
import test_utf8_mode

@unittest.skipIf(test_utf8_mode.MS_WINDOWS, 'Windows has no POSIX locale')
def test_posix_locale():
    code = 'import sys; print(sys.flags.utf8_mode)'
    for loc in test_utf8_mode.POSIX_LOCALES:
        with UTF8ModeTests.subTest(LC_ALL=loc):
            out = UTF8ModeTests.get_output('-c', code, LC_ALL=loc)
            UTF8ModeTests.assertEqual(out, '1')

UTF8ModeTests = test_utf8_mode.UTF8ModeTests()
test_posix_locale()
