import audioop
import sys
import unittest
import test_audioop

def test_findmax():
    TestAudioop.assertEqual(audioop.findmax(test_audioop.datas[2], 1), 5)
    TestAudioop.assertEqual(audioop.findmax(bytearray(test_audioop.datas[2]), 1), 5)
    TestAudioop.assertEqual(audioop.findmax(memoryview(test_audioop.datas[2]), 1), 5)

TestAudioop = test_audioop.TestAudioop()
test_findmax()
