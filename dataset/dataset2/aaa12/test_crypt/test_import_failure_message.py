import sys
import unittest
import crypt
import test_crypt



def test_import_failure_message():
    TestWhyCryptDidNotImport.assertIn('not supported', test_crypt.IMPORT_ERROR)

TestWhyCryptDidNotImport = test_crypt.TestWhyCryptDidNotImport()
test_import_failure_message()
