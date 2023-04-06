import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_aliases():
    aliases = ['SystemAsterisk', 'SystemExclamation', 'SystemExit', 'SystemHand', 'SystemQuestion']
    for alias in aliases:
        with PlaySoundTest.subTest(alias=alias):
            safe_PlaySound(alias, winsound.SND_ALIAS)

PlaySoundTest = test_winsound.PlaySoundTest()
test_aliases()
