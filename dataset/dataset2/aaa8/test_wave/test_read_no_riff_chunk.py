import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_no_riff_chunk():
    b = b'SPAM' + struct.pack('<L', 0)
    with WaveLowLevelTest.assertRaisesRegex(wave.Error, 'file does not start with RIFF id'):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_no_riff_chunk()
