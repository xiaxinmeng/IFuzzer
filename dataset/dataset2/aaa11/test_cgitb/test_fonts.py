from test.support.os_helper import temp_dir
from test.support.script_helper import assert_python_failure
import unittest
import sys
import cgitb
import test_cgitb

def test_fonts():
    text = 'Hello Robbie!'
    TestCgitb.assertEqual(cgitb.small(text), '<small>{}</small>'.format(text))
    TestCgitb.assertEqual(cgitb.strong(text), '<strong>{}</strong>'.format(text))
    TestCgitb.assertEqual(cgitb.grey(text), '<font color="#909090">{}</font>'.format(text))

TestCgitb = test_cgitb.TestCgitb()
test_fonts()
