import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_no_fmt_no_data_chunk():
    b = b'RIFF' + struct.pack('<L', 4) + b'WAVE'
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'fmt chunk and/or data chunk missing'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_no_fmt_no_data_chunk()
