import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_falls_back_to_fallback_if_termios_raises():
    with mock.patch('os.open') as open, mock.patch('io.FileIO') as fileio, mock.patch('io.TextIOWrapper') as textio, mock.patch('termios.tcgetattr'), mock.patch('termios.tcsetattr') as tcsetattr, mock.patch('getpass.fallback_getpass') as fallback:
        open.return_value = 3
        fileio.return_value = BytesIO()
        tcsetattr.side_effect = termios.error
        getpass.unix_getpass()
        fallback.assert_called_once_with('Password: ', textio.return_value)

UnixGetpassTest = test_getpass.UnixGetpassTest()
test_falls_back_to_fallback_if_termios_raises()
