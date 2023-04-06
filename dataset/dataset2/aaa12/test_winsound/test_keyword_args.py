import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_keyword_args():
    safe_PlaySound(flags=winsound.SND_ALIAS, sound='SystemExit')

BeepTest = test_winsound.BeepTest()
test_keyword_args()
