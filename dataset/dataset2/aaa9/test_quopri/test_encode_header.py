import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_encode_header():
    for (p, e) in QuopriTestCase.HSTRINGS:
        QuopriTestCase.assertEqual(quopri.encodestring(p, header=True), e)

QuopriTestCase = test_quopri.QuopriTestCase()
test_encode_header()
