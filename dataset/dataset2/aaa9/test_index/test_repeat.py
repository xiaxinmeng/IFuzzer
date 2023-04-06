import unittest
from test import support
import operator
import test_index

def test_repeat():
    SeqTestCase.o.ind = 3
    SeqTestCase.n.ind = 2
    SeqTestCase.assertEqual(SeqTestCase.seq * SeqTestCase.o, SeqTestCase.seq * 3)
    SeqTestCase.assertEqual(SeqTestCase.seq * SeqTestCase.n, SeqTestCase.seq * 2)
    SeqTestCase.assertEqual(SeqTestCase.o * SeqTestCase.seq, SeqTestCase.seq * 3)
    SeqTestCase.assertEqual(SeqTestCase.n * SeqTestCase.seq, SeqTestCase.seq * 2)

SeqTestCase = test_index.SeqTestCase()
SeqTestCase.setUp()
test_repeat()
