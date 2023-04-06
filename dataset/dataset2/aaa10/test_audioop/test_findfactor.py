import audioop
import sys
import unittest
import test_audioop

def test_findfactor():
    TestAudioop.assertEqual(audioop.findfactor(test_audioop.datas[2], test_audioop.datas[2]), 1.0)
    TestAudioop.assertEqual(audioop.findfactor(bytearray(test_audioop.datas[2]), bytearray(test_audioop.datas[2])), 1.0)
    TestAudioop.assertEqual(audioop.findfactor(memoryview(test_audioop.datas[2]), memoryview(test_audioop.datas[2])), 1.0)
    TestAudioop.assertEqual(audioop.findfactor(b'\x00' * len(test_audioop.datas[2]), test_audioop.datas[2]), 0.0)

TestAudioop = test_audioop.TestAudioop()
test_findfactor()
