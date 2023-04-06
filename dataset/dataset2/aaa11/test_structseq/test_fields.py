import os
import time
import unittest
import test_structseq

def test_fields():
    t = time.gmtime()
    StructSeqTest.assertEqual(len(t), t.n_sequence_fields)
    StructSeqTest.assertEqual(t.n_unnamed_fields, 0)
    StructSeqTest.assertEqual(t.n_fields, time._STRUCT_TM_ITEMS)

StructSeqTest = test_structseq.StructSeqTest()
test_fields()
