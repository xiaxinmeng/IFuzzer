from test import support
from test.support import import_helper
from test.support import findfile
import errno
import sys
import sunau
import time
import audioop
import unittest
from ossaudiodev import AFMT_S16_NE
import test_ossaudiodev

def test_playback():
    sound_info = test_ossaudiodev.read_sound_file(findfile('audiotest.au'))
    OSSAudioDevTests.play_sound_file(*sound_info)

OSSAudioDevTests = test_ossaudiodev.OSSAudioDevTests()
test_playback()
