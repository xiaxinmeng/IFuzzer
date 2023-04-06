import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_resets_termios():
    with mock.patch('os.open') as open, mock.patch('io.FileIO'), mock.patch('io.TextIOWrapper'), mock.patch('termios.tcgetattr') as tcgetattr, mock.patch('termios.tcsetattr') as tcsetattr:
        open.return_value = 3
        fake_attrs = [255, 255, 255, 255, 255]
        tcgetattr.return_value = list(fake_attrs)
        getpass.unix_getpass()
        tcsetattr.assert_called_with(3, mock.ANY, fake_attrs)

UnixGetpassTest = test_getpass.UnixGetpassTest()
test_resets_termios()
