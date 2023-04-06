import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_alias_nofallback():
    safe_PlaySound('!"$%&/(#+*', winsound.SND_ALIAS | winsound.SND_NODEFAULT)

PlaySoundTest = test_winsound.PlaySoundTest()
test_alias_nofallback()
