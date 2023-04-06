from test.support.os_helper import temp_dir
from test.support.script_helper import assert_python_failure
import unittest
import sys
import cgitb
import test_cgitb

def test_blanks():
    TestCgitb.assertEqual(cgitb.small(''), '')
    TestCgitb.assertEqual(cgitb.strong(''), '')
    TestCgitb.assertEqual(cgitb.grey(''), '')

TestCgitb = test_cgitb.TestCgitb()
test_blanks()
