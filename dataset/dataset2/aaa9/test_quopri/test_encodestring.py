import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_encodestring():
    for (p, e) in QuopriTestCase.STRINGS:
        QuopriTestCase.assertEqual(quopri.encodestring(p), e)

QuopriTestCase = test_quopri.QuopriTestCase()
test_encodestring()
