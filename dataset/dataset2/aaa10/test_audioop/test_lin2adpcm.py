import audioop
import sys
import unittest
import test_audioop

def test_lin2adpcm():
    TestAudioop.assertEqual(audioop.lin2adpcm(test_audioop.datas[1], 1, None), (b'\x07\x7f\x7f', (-221, 39)))
    TestAudioop.assertEqual(audioop.lin2adpcm(bytearray(test_audioop.datas[1]), 1, None), (b'\x07\x7f\x7f', (-221, 39)))
    TestAudioop.assertEqual(audioop.lin2adpcm(memoryview(test_audioop.datas[1]), 1, None), (b'\x07\x7f\x7f', (-221, 39)))
    for w in (2, 3, 4):
        TestAudioop.assertEqual(audioop.lin2adpcm(test_audioop.datas[w], w, None), (b'\x07\x7f\x7f', (31, 39)))
    for w in (1, 2, 3, 4):
        TestAudioop.assertEqual(audioop.lin2adpcm(b'\x00' * w * 10, w, None), (b'\x00' * 5, (0, 0)))

TestAudioop = test_audioop.TestAudioop()
test_lin2adpcm()
