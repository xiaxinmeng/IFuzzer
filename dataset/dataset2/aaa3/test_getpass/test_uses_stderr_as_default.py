import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_uses_stderr_as_default():
    input = StringIO('input_string')
    prompt = 'some_prompt'
    with mock.patch('sys.stderr') as stderr:
        getpass._raw_input(prompt, input=input)
        stderr.write.assert_called_once_with(prompt)

GetpassRawinputTest = test_getpass.GetpassRawinputTest()
test_uses_stderr_as_default()
