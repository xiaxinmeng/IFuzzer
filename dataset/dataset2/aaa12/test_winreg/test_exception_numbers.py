import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_exception_numbers():
    with Win64WinregTests.assertRaises(FileNotFoundError) as ctx:
        QueryValue(HKEY_CLASSES_ROOT, 'some_value_that_does_not_exist')

Win64WinregTests = test_winreg.Win64WinregTests()
test_exception_numbers()
