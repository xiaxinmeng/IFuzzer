import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

@mock.patch('sys.stdin')
def test_uses_stdin_as_default_input(GetpassRawinputTest, mock_input):
    mock_input.readline.return_value = 'input_string'
    getpass._raw_input(stream=StringIO())
    mock_input.readline.assert_called_once_with()

GetpassRawinputTest = test_getpass.GetpassRawinputTest()
test_uses_stdin_as_default_input()
