import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_trims_trailing_newline():
    input = StringIO('test\n')
    GetpassRawinputTest.assertEqual('test', getpass._raw_input(input=input))

GetpassRawinputTest = test_getpass.GetpassRawinputTest()
test_trims_trailing_newline()
