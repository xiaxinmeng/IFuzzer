import unittest
from test import audiotests
from audioop import byteswap
import io
import struct
import sys
import sunau
import test_sunau

def test_read_wrong_number_of_channels():
    b = struct.pack('>LLLLLL', sunau.AUDIO_FILE_MAGIC, 24, 0, sunau.AUDIO_FILE_ENCODING_LINEAR_8, 11025, 0)
    with SunauLowLevelTest.assertRaisesRegex(sunau.Error, 'bad # of channels'):
        sunau.open(io.BytesIO(b))

SunauLowLevelTest = test_sunau.SunauLowLevelTest()
test_read_wrong_number_of_channels()
