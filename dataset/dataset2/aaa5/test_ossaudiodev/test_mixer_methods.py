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

def test_mixer_methods():
    with test_ossaudiodev.ossaudiodev.openmixer() as mixer:
        OSSAudioDevTests.assertGreaterEqual(mixer.fileno(), 0)

OSSAudioDevTests = test_ossaudiodev.OSSAudioDevTests()
test_mixer_methods()
