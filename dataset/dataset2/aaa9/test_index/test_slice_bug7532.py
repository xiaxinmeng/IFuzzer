import unittest
from test import support
import operator
import test_index

def test_slice_bug7532():
    seqlen = len(SeqTestCase.seq)
    SeqTestCase.o.ind = int(seqlen * 1.5)
    SeqTestCase.n.ind = seqlen + 2
    SeqTestCase.assertEqual(SeqTestCase.seq[SeqTestCase.o:], SeqTestCase.seq[0:0])
    SeqTestCase.assertEqual(SeqTestCase.seq[:SeqTestCase.o], SeqTestCase.seq)
    SeqTestCase.assertEqual(SeqTestCase.seq[SeqTestCase.n:], SeqTestCase.seq[0:0])
    SeqTestCase.assertEqual(SeqTestCase.seq[:SeqTestCase.n], SeqTestCase.seq)
    SeqTestCase.o2.ind = -seqlen - 2
    SeqTestCase.n2.ind = -int(seqlen * 1.5)
    SeqTestCase.assertEqual(SeqTestCase.seq[SeqTestCase.o2:], SeqTestCase.seq)
    SeqTestCase.assertEqual(SeqTestCase.seq[:SeqTestCase.o2], SeqTestCase.seq[0:0])
    SeqTestCase.assertEqual(SeqTestCase.seq[SeqTestCase.n2:], SeqTestCase.seq)
    SeqTestCase.assertEqual(SeqTestCase.seq[:SeqTestCase.n2], SeqTestCase.seq[0:0])

SeqTestCase = test_index.SeqTestCase()
SeqTestCase.setUp()
test_slice_bug7532()
