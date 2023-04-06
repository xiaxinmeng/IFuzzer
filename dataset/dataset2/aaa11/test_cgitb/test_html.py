from test.support.os_helper import temp_dir
from test.support.script_helper import assert_python_failure
import unittest
import sys
import cgitb
import test_cgitb

def test_html():
    try:
        raise ValueError('Hello World')
    except ValueError as err:
        html = cgitb.html(sys.exc_info())
        TestCgitb.assertIn('ValueError', html)
        TestCgitb.assertIn(str(err), html)

TestCgitb = test_cgitb.TestCgitb()
test_html()
