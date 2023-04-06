import os
import time
import unittest
import test_structseq

def test_contains():
    t1 = time.gmtime()
    for item in t1:
        StructSeqTest.assertIn(item, t1)
    StructSeqTest.assertNotIn(-42, t1)

StructSeqTest = test_structseq.StructSeqTest()
test_contains()
