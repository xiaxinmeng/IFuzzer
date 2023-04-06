import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_hand():
    safe_MessageBeep(winsound.MB_ICONHAND)

MessageBeepTest = test_winsound.MessageBeepTest()
test_hand()
