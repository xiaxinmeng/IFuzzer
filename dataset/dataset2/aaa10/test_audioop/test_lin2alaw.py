import audioop
import sys
import unittest
import test_audioop

def test_lin2alaw():
    TestAudioop.assertEqual(audioop.lin2alaw(test_audioop.datas[1], 1), b'\xd5\x87\xa4$\xaa*Z')
    TestAudioop.assertEqual(audioop.lin2alaw(bytearray(test_audioop.datas[1]), 1), b'\xd5\x87\xa4$\xaa*Z')
    TestAudioop.assertEqual(audioop.lin2alaw(memoryview(test_audioop.datas[1]), 1), b'\xd5\x87\xa4$\xaa*Z')
    for w in (2, 3, 4):
        TestAudioop.assertEqual(audioop.lin2alaw(test_audioop.datas[w], w), b'\xd5\x87\xa4$\xaa*U')

TestAudioop = test_audioop.TestAudioop()
test_lin2alaw()
