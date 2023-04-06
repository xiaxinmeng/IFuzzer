import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_setvalueex_value_range():
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as ck:
            LocalWinregTests.assertNotEqual(ck.handle, 0)
            SetValueEx(ck, 'test_name', None, REG_DWORD, 2147483648)
    finally:
        DeleteKey(HKEY_CURRENT_USER, test_key_name)

LocalWinregTests = test_winreg.LocalWinregTests()
test_setvalueex_value_range()
