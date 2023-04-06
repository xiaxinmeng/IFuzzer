import unittest
import test.badsyntax_pep3120
import test_utf8source

def test_pep3120():
    PEP3120Test.assertEqual('Питон'.encode('utf-8'), b'\xd0\x9f\xd0\xb8\xd1\x82\xd0\xbe\xd0\xbd')
    PEP3120Test.assertEqual('\\П'.encode('utf-8'), b'\\\xd0\x9f')

PEP3120Test = test_utf8source.PEP3120Test()
test_pep3120()
