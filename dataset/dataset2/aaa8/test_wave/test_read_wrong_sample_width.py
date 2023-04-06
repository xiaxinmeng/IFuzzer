import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_wrong_sample_width():
    b = b'RIFF' + struct.pack('<L', 36) + b'WAVE'
    b += b'fmt ' + struct.pack('<LHHLLHH', 16, 1, 1, 11025, 11025, 1, 0)
    b += b'data' + struct.pack('<L', 0)
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'bad sample width'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_wrong_sample_width()
