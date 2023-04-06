import sys
import unittest
import warnings
from test import support
from test.support import warnings_helper
from codeop import compile_command, PyCF_DONT_IMPLY_DEDENT
import io
import test_codeop

def test_valid():
    av = CodeopTests.assertValid
    if not support.is_jython:
        CodeopTests.assertEqual(compile_command(''), compile('pass', '<input>', 'single', PyCF_DONT_IMPLY_DEDENT))
        CodeopTests.assertEqual(compile_command('\n'), compile('pass', '<input>', 'single', PyCF_DONT_IMPLY_DEDENT))
    else:
        av('')
        av('\n')
    av('a = 1')
    av('\na = 1')
    av('a = 1\n')
    av('a = 1\n\n')
    av('\n\na = 1\n\n')
    av('def x():\n  pass\n')
    av('if 1:\n pass\n')
    av('\n\nif 1: pass\n')
    av('\n\nif 1: pass\n\n')
    av('def x():\n\n pass\n')
    av('def x():\n  pass\n  \n')
    av('def x():\n  pass\n \n')
    av('pass\n')
    av('3**3\n')
    av('if 9==3:\n   pass\nelse:\n   pass\n')
    av('if 1:\n pass\n if 1:\n  pass\n else:\n  pass\n')
    av('#a\n#b\na = 3\n')
    av('#a\n\n   \na=3\n')
    av('a=3\n\n')
    av('a = 9+ \\\n3')
    av('3**3', 'eval')
    av('(lambda z: \n z**3)', 'eval')
    av('9+ \\\n3', 'eval')
    av('9+ \\\n3\n', 'eval')
    av('\n\na**3', 'eval')
    av('\n \na**3', 'eval')
    av('#a\n#b\na**3', 'eval')
    av('\n\na = 1\n\n')
    av('\n\nif 1: a=1\n\n')
    av('if 1:\n pass\n if 1:\n  pass\n else:\n  pass\n')
    av('#a\n\n   \na=3\n\n')
    av('\n\na**3', 'eval')
    av('\n \na**3', 'eval')
    av('#a\n#b\na**3', 'eval')
    av('def f():\n try: pass\n finally: [x for x in (1,2)]\n')
    av('def f():\n pass\n#foo\n')
    av('@a.b.c\ndef f():\n pass\n')

CodeopTests = test_codeop.CodeopTests()
test_valid()
