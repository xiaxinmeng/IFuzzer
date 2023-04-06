import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_username_takes_username_from_env(GetpassGetuserTest, environ):
    expected_name = 'some_name'
    environ.get.return_value = expected_name
    GetpassGetuserTest.assertEqual(expected_name, getpass.getuser())

GetpassGetuserTest = test_getpass.GetpassGetuserTest()
test_username_takes_username_from_env()
