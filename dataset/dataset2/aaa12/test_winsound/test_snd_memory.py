import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_snd_memory():
    with open(support.findfile('pluck-pcm8.wav', subdir='audiodata'), 'rb') as f:
        audio_data = f.read()
    safe_PlaySound(audio_data, winsound.SND_MEMORY)
    audio_data = bytearray(audio_data)
    safe_PlaySound(audio_data, winsound.SND_MEMORY)

PlaySoundTest = test_winsound.PlaySoundTest()
test_snd_memory()
