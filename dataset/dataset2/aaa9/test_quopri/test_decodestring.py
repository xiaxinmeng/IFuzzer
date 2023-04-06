import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_decodestring():
    for (p, e) in QuopriTestCase.STRINGS:
        QuopriTestCase.assertEqual(quopri.decodestring(e), p)

QuopriTestCase = test_quopri.QuopriTestCase()
test_decodestring()
