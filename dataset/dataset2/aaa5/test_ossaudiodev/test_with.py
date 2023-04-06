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

def test_with():
    with test_ossaudiodev.ossaudiodev.open('w') as dsp:
        pass
    OSSAudioDevTests.assertTrue(dsp.closed)

OSSAudioDevTests = test_ossaudiodev.OSSAudioDevTests()
test_with()
