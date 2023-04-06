import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound
winsound = import_helper.import_module('winsound')
def test_alias_fallback():
    safe_PlaySound('!"$%&/(#+*', winsound.SND_ALIAS)

PlaySoundTest = test_winsound.PlaySoundTest()
test_alias_fallback()
