import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_remote_registry_works():
    remote_key = ConnectRegistry(REMOTE_NAME, HKEY_CURRENT_USER)
    RemoteWinregTests._test_all(remote_key)

RemoteWinregTests = test_winreg.RemoteWinregTests()
test_remote_registry_works()
