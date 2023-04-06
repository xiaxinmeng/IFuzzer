import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_raises_on_empty_input():
    input = StringIO('')
    GetpassRawinputTest.assertRaises(EOFError, getpass._raw_input, input=input)

GetpassRawinputTest = test_getpass.GetpassRawinputTest()
test_raises_on_empty_input()
