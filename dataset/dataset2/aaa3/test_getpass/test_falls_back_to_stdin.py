import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_falls_back_to_stdin():
    with mock.patch('os.open') as os_open, mock.patch('sys.stdin', spec=StringIO) as stdin:
        os_open.side_effect = IOError
        stdin.fileno.side_effect = AttributeError
        with support.captured_stderr() as stderr:
            with UnixGetpassTest.assertWarns(getpass.GetPassWarning):
                getpass.unix_getpass()
        stdin.readline.assert_called_once_with()
        UnixGetpassTest.assertIn('Warning', stderr.getvalue())
        UnixGetpassTest.assertIn('Password:', stderr.getvalue())

UnixGetpassTest = test_getpass.UnixGetpassTest()
test_falls_back_to_stdin()
