import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_idempotent_string():
    for (p, e) in QuopriTestCase.STRINGS:
        QuopriTestCase.assertEqual(quopri.decodestring(quopri.encodestring(e)), e)

QuopriTestCase = test_quopri.QuopriTestCase()
test_idempotent_string()
