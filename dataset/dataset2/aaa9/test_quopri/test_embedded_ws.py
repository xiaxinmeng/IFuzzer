import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_embedded_ws():
    for (p, e) in QuopriTestCase.ESTRINGS:
        QuopriTestCase.assertEqual(quopri.encodestring(p, quotetabs=True), e)
        QuopriTestCase.assertEqual(quopri.decodestring(e), p)

QuopriTestCase = test_quopri.QuopriTestCase()
test_embedded_ws()
