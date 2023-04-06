import os
import time
import unittest
import test_structseq

def test_eviltuple():

    class Exc(Exception):
        pass

    class C:

        def __getitem__(StructSeqTest, i):
            raise Exc

        def __len__(StructSeqTest):
            return 9
    StructSeqTest.assertRaises(Exc, time.struct_time, C())

StructSeqTest = test_structseq.StructSeqTest()
test_eviltuple()
