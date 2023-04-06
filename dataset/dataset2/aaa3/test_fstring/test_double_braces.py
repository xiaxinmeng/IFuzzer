import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_double_braces():
    TestCase.assertEqual(f'{{', '{')
    TestCase.assertEqual(f'a{{', 'a{')
    TestCase.assertEqual(f'{{b', '{b')
    TestCase.assertEqual(f'a{{b', 'a{b')
    TestCase.assertEqual(f'}}', '}')
    TestCase.assertEqual(f'a}}', 'a}')
    TestCase.assertEqual(f'}}b', '}b')
    TestCase.assertEqual(f'a}}b', 'a}b')
    TestCase.assertEqual(f'{{}}', '{}')
    TestCase.assertEqual(f'a{{}}', 'a{}')
    TestCase.assertEqual(f'{{b}}', '{b}')
    TestCase.assertEqual(f'{{}}c', '{}c')
    TestCase.assertEqual(f'a{{b}}', 'a{b}')
    TestCase.assertEqual(f'a{{}}c', 'a{}c')
    TestCase.assertEqual(f'{{b}}c', '{b}c')
    TestCase.assertEqual(f'a{{b}}c', 'a{b}c')
    TestCase.assertEqual(f'{{{10}', '{10')
    TestCase.assertEqual(f'}}{10}', '}10')
    TestCase.assertEqual(f'}}{{{10}', '}{10')
    TestCase.assertEqual(f'}}a{{{10}', '}a{10')
    TestCase.assertEqual(f'{10}{{', '10{')
    TestCase.assertEqual(f'{10}}}', '10}')
    TestCase.assertEqual(f'{10}}}{{', '10}{')
    TestCase.assertEqual(f'{10}}}a{{}}', '10}a{}')
    TestCase.assertEqual(f"{'{{}}'}", '{{}}')
    TestCase.assertAllRaise(TypeError, 'unhashable type', ["f'{ {{}} }'"])

TestCase = test_fstring.TestCase()
test_double_braces()
