import __future__
import unittest
from test import support
import test_flufl

def test_guido_as_bdfl():
    code = '2 {0} 3'
    compile(code.format('!='), '<BDFL test>', 'exec')
    with FLUFLTests.assertRaises(SyntaxError) as cm:
        compile(code.format('<>'), '<FLUFL test>', 'exec')
    FLUFLTests.assertRegex(str(cm.exception), 'invalid syntax')
    FLUFLTests.assertIn('2 <> 3', cm.exception.text)
    FLUFLTests.assertEqual(cm.exception.filename, '<FLUFL test>')
    FLUFLTests.assertEqual(cm.exception.lineno, 1)
    FLUFLTests.assertEqual(cm.exception.offset, 3)

FLUFLTests = test_flufl.FLUFLTests()
test_guido_as_bdfl()
