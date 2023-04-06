import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition

import test_winreg

def test_context_manager():
    try:
        with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as h:
            LocalWinregTests.assertNotEqual(h.handle, 0)
            raise OSError
    except OSError:
        LocalWinregTests.assertEqual(h.handle, 0)

LocalWinregTests = test_winreg.LocalWinregTests()
test_context_manager()
