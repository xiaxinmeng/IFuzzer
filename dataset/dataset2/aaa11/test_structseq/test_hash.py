import os
import time
import unittest
import test_structseq

def test_hash():
    t1 = time.gmtime()
    StructSeqTest.assertEqual(hash(t1), hash(tuple(t1)))

StructSeqTest = test_structseq.StructSeqTest()
test_hash()
