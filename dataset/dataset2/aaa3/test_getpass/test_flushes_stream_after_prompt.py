import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_flushes_stream_after_prompt():
    stream = mock.Mock(spec=StringIO)
    input = StringIO('input_string')
    getpass._raw_input('some_prompt', stream, input=input)
    stream.flush.assert_called_once_with()

GetpassRawinputTest = test_getpass.GetpassRawinputTest()
test_flushes_stream_after_prompt()
