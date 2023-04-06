import unittest
import string
from string import Template
import test_string

def test_invalid_with_no_lines():

    class MyTemplate(Template):
        pattern = '\n              (?P<invalid>) |\n              unreachable(\n                (?P<named>)   |\n                (?P<braced>)  |\n                (?P<escaped>)\n              )\n            '
    s = MyTemplate('')
    with TestTemplate.assertRaises(ValueError) as err:
        s.substitute({})
    TestTemplate.assertIn('line 1, col 1', str(err.exception))

TestTemplate = test_string.TestTemplate()
test_invalid_with_no_lines()
