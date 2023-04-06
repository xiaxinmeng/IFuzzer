import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_dynamic_key():
    try:
        EnumValue(HKEY_PERFORMANCE_DATA, 0)
    except OSError as e:
        if e.errno in (errno.EPERM, errno.EACCES):
            LocalWinregTests.skipTest('access denied to registry key (are you running in a non-interactive session?)')
        raise
    QueryValueEx(HKEY_PERFORMANCE_DATA, '')

LocalWinregTests = test_winreg.LocalWinregTests()
test_dynamic_key()
