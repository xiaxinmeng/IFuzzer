import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition

import test_winreg

def test_connect_registry_to_local_machine_works():
    h = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    LocalWinregTests.assertNotEqual(h.handle, 0)
    h.Close()
    LocalWinregTests.assertEqual(h.handle, 0)

LocalWinregTests = test_winreg.LocalWinregTests()
test_connect_registry_to_local_machine_works()
