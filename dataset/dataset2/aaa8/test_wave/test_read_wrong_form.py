import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_wrong_form():
    b = b'RIFF' + struct.pack('<L', 36) + b'WAVE'
    b += b'fmt ' + struct.pack('<LHHLLHH', 16, 2, 1, 11025, 11025, 1, 1)
    b += b'data' + struct.pack('<L', 0)
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'unknown format: 2'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_wrong_form()
