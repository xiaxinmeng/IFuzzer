import __future__
import unittest
from test import support
import test_flufl

def test_barry_as_bdfl():
    code = 'from __future__ import barry_as_FLUFL\n2 {0} 3'
    compile(code.format('<>'), '<BDFL test>', 'exec', __future__.CO_FUTURE_BARRY_AS_BDFL)
    with FLUFLTests.assertRaises(SyntaxError) as cm:
        compile(code.format('!='), '<FLUFL test>', 'exec', __future__.CO_FUTURE_BARRY_AS_BDFL)
    FLUFLTests.assertRegex(str(cm.exception), "with Barry as BDFL, use '<>' instead of '!='")
    FLUFLTests.assertIn('2 != 3', cm.exception.text)
    FLUFLTests.assertEqual(cm.exception.filename, '<FLUFL test>')
    FLUFLTests.assertTrue(cm.exception.lineno, 2)
    FLUFLTests.assertEqual(cm.exception.offset, 3)

FLUFLTests = test_flufl.FLUFLTests()
test_barry_as_bdfl()
