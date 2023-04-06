import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_snd_filename():
    fn = support.findfile('pluck-pcm8.wav', subdir='audiodata')
    safe_PlaySound(fn, winsound.SND_FILENAME | winsound.SND_NODEFAULT)

PlaySoundTest = test_winsound.PlaySoundTest()
test_snd_filename()
