import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_stopasync():
    safe_PlaySound('SystemQuestion', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
    time.sleep(0.5)
    safe_PlaySound('SystemQuestion', winsound.SND_ALIAS | winsound.SND_NOSTOP)
    winsound.PlaySound(None, winsound.SND_PURGE)

PlaySoundTest = test_winsound.PlaySoundTest()
test_stopasync()
