import getpass
import os
import unittest
from io import BytesIO, StringIO, TextIOWrapper
from unittest import mock
from test import support
import termios
import pwd
import test_getpass

def test_username_priorities_of_env_values(GetpassGetuserTest, environ):
    environ.get.return_value = None
    try:
        getpass.getuser()
    except ImportError:
        pass
    GetpassGetuserTest.assertEqual(environ.get.call_args_list, [mock.call(x) for x in ('LOGNAME', 'USER', 'LNAME', 'USERNAME')])

GetpassGetuserTest = test_getpass.GetpassGetuserTest()
test_username_priorities_of_env_values()
