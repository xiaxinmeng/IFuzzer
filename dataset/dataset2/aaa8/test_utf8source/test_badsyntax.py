import unittest
import test.badsyntax_pep3120
import test_utf8source

def test_badsyntax():
    try:
        import test.badsyntax_pep3120
    except SyntaxError as msg:
        msg = str(msg).lower()
        PEP3120Test.assertTrue('utf-8' in msg)
    else:
        PEP3120Test.fail("expected exception didn't occur")

PEP3120Test = test_utf8source.PEP3120Test()
test_badsyntax()
