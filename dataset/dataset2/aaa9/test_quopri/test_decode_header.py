import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_decode_header():
    for (p, e) in QuopriTestCase.HSTRINGS:
        QuopriTestCase.assertEqual(quopri.decodestring(e, header=True), p)

QuopriTestCase = test_quopri.QuopriTestCase()
test_decode_header()
