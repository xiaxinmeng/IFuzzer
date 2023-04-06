import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_uses_tty_directly():
    with mock.patch('os.open') as open, mock.patch('io.FileIO') as fileio, mock.patch('io.TextIOWrapper') as textio:
        open.return_value = None
        getpass.unix_getpass()
        open.assert_called_once_with('/dev/tty', os.O_RDWR | os.O_NOCTTY)
        fileio.assert_called_once_with(open.return_value, 'w+')
        textio.assert_called_once_with(fileio.return_value)

UnixGetpassTest = test_getpass.UnixGetpassTest()
test_uses_tty_directly()
