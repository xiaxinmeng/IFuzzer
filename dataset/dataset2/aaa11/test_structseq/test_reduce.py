import os
import time
import unittest
import test_structseq

def test_reduce():
    t = time.gmtime()
    x = t.__reduce__()

StructSeqTest = test_structseq.StructSeqTest()
test_reduce()
