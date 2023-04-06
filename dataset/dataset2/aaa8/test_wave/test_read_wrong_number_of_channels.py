import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_wrong_number_of_channels():
    b = b'RIFF' + struct.pack('<L', 36) + b'WAVE'
    b += b'fmt ' + struct.pack('<LHHLLHH', 16, 1, 0, 11025, 11025, 1, 8)
    b += b'data' + struct.pack('<L', 0)
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'bad # of channels'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_wrong_number_of_channels()
