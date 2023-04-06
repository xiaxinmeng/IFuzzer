import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_encode():
    for (p, e) in QuopriTestCase.STRINGS:
        infp = io.BytesIO(p)
        outfp = io.BytesIO()
        quopri.encode(infp, outfp, quotetabs=False)
        QuopriTestCase.assertEqual(outfp.getvalue(), e)

QuopriTestCase = test_quopri.QuopriTestCase()
test_encode()
