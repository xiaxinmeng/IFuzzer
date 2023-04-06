import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_no_fmt_chunk():
    b = b'RIFF' + struct.pack('<L', 12) + b'WAVE'
    b += b'data' + struct.pack('<L', 0)
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'data chunk before fmt chunk'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_no_fmt_chunk()
