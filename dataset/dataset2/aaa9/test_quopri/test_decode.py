import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_decode():
    for (p, e) in QuopriTestCase.STRINGS:
        infp = io.BytesIO(e)
        outfp = io.BytesIO()
        quopri.decode(infp, outfp)
        QuopriTestCase.assertEqual(outfp.getvalue(), p)

QuopriTestCase = test_quopri.QuopriTestCase()
test_decode()
