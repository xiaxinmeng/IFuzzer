from test.support.os_helper import temp_dir
from test.support.script_helper import assert_python_failure
import unittest
import sys
import cgitb
import test_cgitb

def test_text():
    try:
        raise ValueError('Hello World')
    except ValueError:
        text = cgitb.text(sys.exc_info())
        TestCgitb.assertIn('ValueError', text)
        TestCgitb.assertIn('Hello World', text)

TestCgitb = test_cgitb.TestCgitb()
test_text()
