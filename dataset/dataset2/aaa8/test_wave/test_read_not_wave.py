import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_not_wave():
    b = b'RIFF' + struct.pack('<L', 4) + b'SPAM'
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'not a WAVE file'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_not_wave()
