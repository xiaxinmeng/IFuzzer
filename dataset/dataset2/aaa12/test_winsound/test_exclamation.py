import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_exclamation():
    safe_MessageBeep(winsound.MB_ICONEXCLAMATION)

MessageBeepTest = test_winsound.MessageBeepTest()
test_exclamation()
