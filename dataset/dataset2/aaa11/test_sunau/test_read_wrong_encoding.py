import unittest
from test import audiotests
from audioop import byteswap
import io
import struct
import sys
import sunau
import test_sunau

def test_read_wrong_encoding():
    b = struct.pack('>LLLLLL', sunau.AUDIO_FILE_MAGIC, 24, 0, 0, 11025, 1)
    with SunauLowLevelTest.assertRaisesRegex(sunau.Error, 'encoding not \\(yet\\) supported'):
        sunau.open(io.BytesIO(b))

SunauLowLevelTest = test_sunau.SunauLowLevelTest()
test_read_wrong_encoding()
