import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_flushes_stream_after_input():
    with mock.patch('os.open') as open, mock.patch('io.FileIO'), mock.patch('io.TextIOWrapper'), mock.patch('termios.tcgetattr'), mock.patch('termios.tcsetattr'):
        open.return_value = 3
        mock_stream = mock.Mock(spec=StringIO)
        getpass.unix_getpass(stream=mock_stream)
        mock_stream.flush.assert_called_with()

UnixGetpassTest = test_getpass.UnixGetpassTest()
test_flushes_stream_after_input()
