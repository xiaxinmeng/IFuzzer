import audioop
import sys
import unittest
import test_audioop

def test_lin2ulaw():
    TestAudioop.assertEqual(audioop.lin2ulaw(test_audioop.datas[1], 1), b'\xff\xad\x8e\x0e\x80\x00g')
    TestAudioop.assertEqual(audioop.lin2ulaw(bytearray(test_audioop.datas[1]), 1), b'\xff\xad\x8e\x0e\x80\x00g')
    TestAudioop.assertEqual(audioop.lin2ulaw(memoryview(test_audioop.datas[1]), 1), b'\xff\xad\x8e\x0e\x80\x00g')
    for w in (2, 3, 4):
        TestAudioop.assertEqual(audioop.lin2ulaw(test_audioop.datas[w], w), b'\xff\xad\x8e\x0e\x80\x00~')

TestAudioop = test_audioop.TestAudioop()
test_lin2ulaw()
